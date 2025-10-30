# Archivo: codegen/PythonCodeGenerator.py

import textwrap
import sys

class PythonCodeGenerator:
    def __init__(self):
        self.code = []
        self.indent_level = 0
        self.tabs = '    '
        self.scene_names = set() 

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1

    def emit(self, line=""):
        if not line:
            self.code.append("")
            return
        
        if '\n' in line:
            clean_lines = textwrap.dedent(line).split('\n')
            for l in clean_lines:
                 self.code.append(self.tabs * self.indent_level + l)
        else:
            self.code.append(self.tabs * self.indent_level + line)

    def emit_header(self):
        """Genera el encabezado y las variables globales de estado."""
        self.emit("#!/usr/bin/env python3")
        self.emit("# Compilado por Mini-Compilador GuionesLang (Fase 5)")
        self.emit("import sys")
        self.emit("import time")
        self.emit("")
        self.emit("current_item = 'Mano'")
        self.emit("inventario = ['Mano']")
        self.emit("")
        
    def emit_function_start(self, name):
        """Define el inicio de una escena/función."""
        self.scene_names.add(name)
        self.emit(f"def {name}():")
        self.indent()
        # Declarar variables globales dentro de la función para poder modificarlas
        self.emit("global current_item, inventario") 

    def emit_function_end(self):
        self.dedent()
        self.emit("")

    def emit_print(self, text):
        """Traduce 'decir STRING;' a print(STRING)."""
        self.emit(f"print({text})")
        
    def emit_state_change(self, item_id):
        """Traduce 'obtener_item ID;' a una actualización de la variable global."""
        self.emit(f"current_item = '{item_id}'")
        self.emit(f"if '{item_id}' not in inventario: inventario.append('{item_id}')")
        self.emit(f"print(f'\\n[ITEM]: ¡Obtenido {item_id}! Estado actual: {{current_item}}')")
        
    def emit_option(self, option_text, target_id):
        """Traduce 'opcion STRING ir_a ID;' a input() y lógica de salto."""
        self.emit(f"print('\\n--- Opciones ---')")
        self.emit(f"choice = input(f'[Opción: {option_text.strip('\"')} (Escribe 1 o {option_text})] -> ')")
        
        self.emit(f"if choice.strip().lower() in ['1', {option_text}.lower().strip('\"')]:")
        self.indent()
        self.emit(f"{target_id}()") 
        self.dedent()
        self.emit("else:")
        self.indent()
        self.emit("print('Opción inválida. Reintentando...')")
        self.emit(f"globals()[sys._getframe(0).f_code.co_name]()") 
        self.dedent()
        
    def emit_main_call(self, start_scene):
        """Genera el bloque de inicio del programa."""
        self.emit("")
        self.emit("if __name__ == '__main__':")
        self.indent()
        self.emit("try:")
        self.indent()
        self.emit(f"{start_scene}()")
        self.dedent()
        self.emit("except RecursionError:")
        self.indent()
        self.emit("print('\\n[ERROR]: El juego ha entrado en un bucle infinito.')")
        self.dedent()
        self.emit("except KeyboardInterrupt:")
        self.indent()
        self.emit("print('\\n[FIN DEL JUEGO]...')")
        self.dedent()
        self.dedent()

    def get_code(self):
        return '\n'.join(self.code)