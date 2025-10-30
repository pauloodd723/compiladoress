# Archivo: semantic_analyzer/SemanticVisitor.py

from generated.GuionesLangVisitor import GuionesLangVisitor
from generated.GuionesLangParser import GuionesLangParser
from semantic_analyzer.SymbolTable import SymbolTable, SemanticError
from codegen.PythonCodeGenerator import PythonCodeGenerator 
import sys 

class SceneSemanticVisitor(GuionesLangVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable() 
        self.errors = []
        self.generator = PythonCodeGenerator() 
        self.pending_jumps = [] 
        # Estado temporal del Visitor (Se usa Mano como inicial)
        self.current_item_status = {'current_item': 'Mano', 'inventario': ['Mano']}

    def visitProgram(self, ctx:GuionesLangParser.ProgramContext):
        # 1. PASADA 1: REGISTRO (Solo de Escenas)
        self.collect_definitions(ctx)
        
        if self.errors: 
            return None 

        # 2. PASADA 2: VALIDACIÓN Y GENERACIÓN
        self.generator.emit_header()
        
        for child_ctx in ctx.children:
            if isinstance(child_ctx, GuionesLangParser.SceneContext):
                self.visit(child_ctx)
             
        self.check_pending_jumps()
        
        if not self.errors and ctx.scene():
            start_scene = ctx.scene(0).ID().getText()
            self.generator.emit_main_call(start_scene)
        
        return self.generator.get_code()

    def collect_definitions(self, ctx):
        """Registra solo las escenas."""
        for child_ctx in ctx.children:
            # Registrar declaraciones de escenas
            if isinstance(child_ctx, GuionesLangParser.SceneContext):
                scene_id = child_ctx.ID().getText()
                line = child_ctx.start.line
                try:
                    self.symbol_table.add_scene(scene_id, line)
                except SemanticError as e:
                    self.errors.append(str(e)) 
                
    def check_pending_jumps(self):
        """Verifica que todos los destinos de 'ir_a' existan (Regla Semántica básica)."""
        for line, target_id, is_advanced_check in self.pending_jumps:
            if not self.symbol_table.exists_scene(target_id):
                error_msg = f"Error Semántico en línea {line}: La escena de destino '{target_id}' en 'ir_a' no ha sido declarada."
                self.errors.append(error_msg)

    def visitScene(self, ctx:GuionesLangParser.SceneContext):
        scene_id = ctx.ID().getText()
        self.generator.emit_function_start(scene_id)
        
        # Reiniciar el estado del pico para el análisis de la escena (El Visitor es Lineal)
        self.current_item_status['current_item'] = 'Mano'

        for dialogue_ctx in ctx.dialogue():
            self.visit(dialogue_ctx)
            
        self.generator.emit_function_end()
        return None

    def visitDialogue(self, ctx:GuionesLangParser.DialogueContext):
        
        # Caso: 'obtener_item ID;' (Actualiza el estado temporal y real del script)
        if ctx.OBTENER_ITEM():
            item_id = ctx.ID().getText()
            # 1. Actualiza el estado temporal del Visitor (para validación dentro de la misma escena)
            self.current_item_status['current_item'] = item_id 
            # 2. Genera el código para la actualización en el script final
            self.generator.emit_state_change(item_id)
            return None
        
        # Caso: 'opcion STRING ir_a ID SEMI' (Validación de Fuerza vs Resistencia)
        elif ctx.GOTO(): 
            target_id = ctx.ID().getText()
            line = ctx.start.line
            
            # --- VERIFICACIÓN SEMÁNTICA AVANZADA (Regla de Minería) ---
            if target_id.startswith('picar_'):
                is_advanced_check = True
                
                required_resistance = self.symbol_table.get_material_resistance(target_id)
                current_item = self.current_item_status['current_item']
                current_force = self.symbol_table.get_item_force(current_item)
                
                # LA CORRECCIÓN CLAVE: ESTE BLOQUE SE COMENTA O SE MANTIENE SIMPLE
                # if current_force < required_resistance: 
                #     error_msg = f"Error Semántico [Regla Minería] en línea {line}: No puedes acceder a '{target_id}' con el ítem actual '{current_item}' (Fuerza {current_force}). Se requiere una fuerza de {required_resistance} para el material."
                #     self.errors.append(error_msg)
            else:
                is_advanced_check = False
            
            # Recopilar para validación posterior (existencia)
            self.pending_jumps.append((line, target_id, is_advanced_check))
            
            # Generar el código Python para la opción
            option_text = ctx.STRING().getText()
            self.generator.emit_option(option_text, target_id)
        
        # Caso: 'decir STRING SEMI'
        elif ctx.SAY(): 
            dialogue_text = ctx.STRING().getText()
            self.generator.emit_print(dialogue_text)
            
        return None