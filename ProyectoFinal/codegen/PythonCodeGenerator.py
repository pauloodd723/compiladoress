# Archivo: codegen/PythonCodeGenerator.py

import textwrap
import sys

class PythonCodeGenerator:
    """
    Implementa la Fase 4/5 (Generación de Código Final).
    Traduce las sentencias del lenguaje de guiones a código Python ejecutable.
    """
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
        """Añade una línea con la indentación apropiada."""
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
        self.emit("# Proyecto Final - Compiladores")
        self.emit("import sys")
        self.emit("import time")
        self.emit("")
        # Variables de estado globales que reflejan el estado del juego
        self.emit("current_item = 'Mano'")
        self.emit("inventario = ['Mano']")
        self.emit("item_properties = {")
        self.emit("    # Incluye aquí la tabla de propiedades si fuera necesaria en tiempo de ejecución")
        self.emit("}")
        self.emit("")
        
    def emit_function_start(self, name):
        """Define el inicio de una escena/función."""
        self.scene_names.add(name)
        self.emit(f"def {name}():")
        self.indent()
        self.emit("global current_item, inventario") 

    def emit_function_end(self):
        """Cierra el bloque de la función."""
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
        """Traduce 'opcion STRING ir_a ID;' a input() y lógica de salto simple."""
        
        # 1. Mostrar las opciones disponibles
        self.emit(f"print('\\n--- Opciones ---')")
        self.emit(f"print(f' 1. {option_text.strip('\"')}')")
        
        # 2. Capturar la entrada del usuario
        self.emit(f"choice = input(f'[Elige tu acción (1 o texto de la opción)] -> ')")

        # 3. Lógica de salto (IF/ELSE)
        self.emit(f"if choice.strip().lower() in ['1', {option_text}.lower().strip('\"')]:")
        self.indent()
        self.emit(f"print(f'\\n>> [Saltando a {target_id}]...')")
        self.emit(f"{target_id}()") # Llama a la siguiente función
        self.emit("return") # Sale de la función actual
        self.dedent()
        
        self.emit("else:")
        self.indent()
        # Si la opción no es válida, regresa a la escena actual (bucle)
        self.emit("print('Opción inválida. Regresando a la escena.')")
        # Llama a la función actual por su nombre para reintentar (bucle)
        self.emit(f"globals()[sys._getframe(0).f_code.co_name]()") 
        self.dedent()

    def emit_main_call(self, start_scene):
        """Genera el bloque de inicio del programa."""
        self.emit("")
        self.emit("if __name__ == '__main__':")
        self.indent()
        self.emit("try:")
        self.indent()
        self.emit(f"print('--- JUEGO INICIADO ---')")
        self.emit(f"time.sleep(0.5)")
        self.emit(f"{start_scene}()")
        self.dedent()
        self.emit("except Exception as e:")
        self.indent()
        self.emit("print(f'\\n[ERROR FATAL DE EJECUCIÓN]: {e}')")
        self.dedent()
        self.emit("except KeyboardInterrupt:")
        self.indent()
        self.emit("print('\\n[FIN DEL JUEGO]...')")
        self.dedent()
        self.dedent()

    def get_code(self):
        """Devuelve el código Python final como una cadena."""
        return '\n'.join(self.code)