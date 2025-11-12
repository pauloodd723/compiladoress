# codegen/PythonCodeGenerator.py

class PythonCodeGenerator:
    """
    Genera un script Python a partir del TAC.
    """
    def __init__(self, tac_instructions):
        self.tac = tac_instructions
        self.python_code = []
        self.indent_level = 0

    def emit(self, line=""):
        indent = "    " * self.indent_level
        self.python_code.append(indent + line)

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1

    def generate(self):
        self.emit("# --- Código Python Generado Automáticamente ---\n")

        # Generar funciones de escenas
        scene_functions = {}
        current_func = None

        for inst in self.tac:
            op = inst['op']
            if op.startswith("L_SCENE_"):
                func_name = op.replace("L_SCENE_", "").replace(":", "")
                current_func = func_name
                scene_functions[func_name] = []
            elif op == "RETURN":
                scene_functions[current_func].append("return")
            elif op == "PRINT":
                scene_functions[current_func].append(f'print("{inst["arg1"]}")')
            elif op == "INPUT":
                scene_functions[current_func].append(f'{inst["result"]} = input("{inst["arg1"]} -> ")')
            elif op == "IF_OPTION":
                scene_functions[current_func].append(f'if {inst["arg1"]} == "{inst["arg2"]}":')
                scene_functions[current_func].append(f'    {inst["result"]}()')

        # Emitir funciones
        self.emit("# --- Definición de Escenas (Funciones) ---")
        for func_name, lines in scene_functions.items():
            self.emit(f"\ndef {func_name}():")
            self.indent()
            for line in lines:
                self.emit(line)
            self.dedent()

        # Punto de entrada
        self.emit("\n# --- Punto de Entrada ---")
        self.emit("if __name__ == '__main__':")
        self.indent()
        first_scene = list(scene_functions.keys())[0]
        self.emit("print('--- Iniciando Juego ---')")
        self.emit(f"{first_scene}()")
        self.emit("print('--- Fin del Juego ---')")
        self.dedent()

        return "\n".join(self.python_code)
