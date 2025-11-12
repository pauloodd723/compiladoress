# semantic_analyzer/SemanticAnalyzerVisitor.py

from generated.gramaticaVisitor import gramaticaVisitor
from generated.gramaticaParser import gramaticaParser

class TAC:
    """
    Representa las instrucciones intermedias del compilador.
    """
    def __init__(self):
        self.instructions = []

    def add(self, instr):
        self.instructions.append(instr)


class SymbolTable:
    """
    Tabla de símbolos para escenas.
    """
    def __init__(self):
        self.scenes = {}  # nombre_escena -> objeto de escena


class SemanticAnalyzerVisitor(gramaticaVisitor):
    """
    Analizador semántico y generador de TAC.
    """
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.ir = TAC()
        self.current_scene = None

    # --- Visitar el programa completo ---
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        for scene in ctx.scene():
            self.visit(scene)
        return self.ir

    # --- Visitar cada escena ---
    def visitScene(self, ctx:gramaticaParser.SceneContext):
        scene_name = ctx.ID().getText()
        if scene_name in self.symbol_table.scenes:
            raise Exception(f"Error semántico: Escena duplicada '{scene_name}'")
        self.symbol_table.scenes[scene_name] = ctx
        self.current_scene = scene_name

        # Etiqueta de escena
        self.ir.add({'op': f"L_SCENE_{scene_name}:"})

        # Para controlar opciones duplicadas dentro de la escena
        option_texts = set()

        # Visitar diálogos
        for dlg in ctx.dialogue():
            if dlg.OPCION():
                option_text = dlg.STRING().getText().strip('"')
                if option_text in option_texts:
                    raise Exception(f"Error semántico: Opción duplicada '{option_text}' en escena '{scene_name}'")
                option_texts.add(option_text)
            self.visit(dlg)

        # RETURN al final de escena
        self.ir.add({'op': 'RETURN'})
        return self.ir

    # --- Visitar diálogos ---
    def visitDialogue(self, ctx:gramaticaParser.DialogueContext):
        if ctx.DECIR():
            # texto del decir
            text = ctx.STRING().getText().strip('"')
            self.ir.add({'op': 'PRINT', 'arg1': text})
        elif ctx.OPCION():
            # texto de la opción
            option_text = ctx.STRING().getText().strip('"')
            target_scene = ctx.ID().getText()

            # --- VERIFICACIÓN: Escena de destino existe ---
        #  if target_scene not in self.symbol_table.scenes:
           #     raise Exception(f"Error semántico: Escena inexistente '{target_scene}'")

            # input + if_option
            temp_var = f"op_{len(self.ir.instructions)}"
            self.ir.add({'op': 'INPUT', 'arg1': option_text, 'result': temp_var})
            self.ir.add({'op': 'IF_OPTION', 'arg1': temp_var, 'arg2': option_text, 'result': target_scene})
        else:
            raise Exception("Error semántico: diálogo desconocido")
        return self.ir
