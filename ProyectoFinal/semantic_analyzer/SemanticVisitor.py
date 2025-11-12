# Archivo: semantic_analyzer/SemanticVisitor.py

from generated.GuionesLangVisitor import GuionesLangVisitor
from generated.GuionesLangParser import GuionesLangParser
from semantic_analyzer.SymbolTable import SemanticError
# Nota: Recibiremos la instancia del Generador de Código y SymbolTable en el __init__

class SceneSemanticVisitor(GuionesLangVisitor):
    def __init__(self, symbol_table_instance, code_generator_instance):
        self.symbol_table = symbol_table_instance
        self.generator = code_generator_instance
        self.errors = []
        self.pending_jumps = [] 
        # Estado temporal del Visitor (se usa la Mano como ítem inicial para cada escena)
        self.current_item_status = {'current_item': 'Mano', 'inventario': ['Mano']}

    def visitProgram(self, ctx:GuionesLangParser.ProgramContext):
        self.collect_declarations(ctx)
        
        if self.errors: return None 

        self.generator.emit_header()
        
        for child_ctx in ctx.children:
            if isinstance(child_ctx, GuionesLangParser.SceneContext):
                self.visit(child_ctx)
             
        self.check_pending_jumps()
        
        if not self.errors and ctx.scene():
            start_scene = ctx.scene(0).ID().getText()
            self.generator.emit_main_call(start_scene)
        
        return self.generator.get_code()

    def collect_declarations(self, ctx):
        """Registra solo las escenas."""
        for child_ctx in ctx.children:
            if isinstance(child_ctx, GuionesLangParser.SceneContext):
                scene_id = child_ctx.ID().getText()
                line = child_ctx.start.line
                try:
                    self.symbol_table.add_scene(scene_id, line)
                except SemanticError as e:
                    self.errors.append(str(e)) 

    def check_pending_jumps(self):
        """Verifica que todos los destinos de 'ir_a' existan (Regla Semántica)."""
        for line, target_id, is_advanced_check in self.pending_jumps:
            if not self.symbol_table.exists_scene(target_id):
                error_msg = f"Error Semántico en línea {line}: La escena de destino '{target_id}' en 'ir_a' no ha sido declarada."
                self.errors.append(error_msg)

    def visitScene(self, ctx:GuionesLangParser.SceneContext):
        scene_id = ctx.ID().getText()
        self.generator.emit_function_start(scene_id)
        
        # Reiniciar el estado del pico para el análisis de la escena 
        self.current_item_status['current_item'] = 'Mano'

        for dialogue_ctx in ctx.dialogue():
            self.visit(dialogue_ctx)
            
        self.generator.emit_function_end()
        return None

    def visitDialogue(self, ctx:GuionesLangParser.DialogueContext):
        
        if ctx.OBTENER_ITEM():
            item_id = ctx.ID().getText()
            # 1. Actualiza el estado temporal del Visitor (para validación de minería dentro de la misma escena)
            self.current_item_status['current_item'] = item_id 
            # 2. Genera el código para la actualización en el script final
            self.generator.emit_state_change(item_id)
            return None
        
        elif ctx.GOTO(): 
            target_id = ctx.ID().getText()
            line = ctx.start.line
            
            # --- VERIFICACIÓN SEMÁNTICA AVANZADA (Regla de Minería) ---
            if target_id.startswith('picar_'):
                is_advanced_check = True
                
                required_resistance = self.symbol_table.get_material_resistance(target_id)
                current_item = self.current_item_status['current_item']
                current_force = self.symbol_table.get_item_force(current_item)
                
                # Regla: La fuerza del ítem actual debe ser >= a la resistencia requerida
                if current_force < required_resistance: 
                    error_msg = f"Error Semántico [Regla Minería] en línea {line}: No puedes acceder a '{target_id}' con el ítem actual '{current_item}' (Fuerza {current_force}). Se requiere una fuerza de {required_resistance} para el material."
                    self.errors.append(error_msg)
            else:
                is_advanced_check = False
            
            # Recopilar para validación posterior (existencia)
            self.pending_jumps.append((line, target_id, is_advanced_check))
            
            # Generar el código Python para la opción
            option_text = ctx.STRING().getText()
            self.generator.emit_option(option_text, target_id)
        
        elif ctx.SAY(): 
            dialogue_text = ctx.STRING().getText()
            self.generator.emit_print(dialogue_text)
            
        return None