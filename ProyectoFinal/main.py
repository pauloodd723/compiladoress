from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
import csv
import sys
import subprocess
import os

# Asegúrate que estas importaciones coincidan con el nombre de tu gramática (GuionesLang)
from generated.GuionesLangLexer import GuionesLangLexer
from generated.GuionesLangParser import GuionesLangParser
from semantic_analyzer.SemanticVisitor import SceneSemanticVisitor
from semantic_analyzer.SymbolTable import SemanticError

# --- CONFIGURACIÓN DE ERRORES SINTÁCTICOS/LÉXICOS ---
class SyntaxErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error Sintáctico/Léxico en línea {line}:{column}: {msg}")

# --- FUNCIÓN AUXILIAR PARA EL REPORTE (Añadida) ---
def pretty_tree(node, rule_names, level=0):
    """Imprime el árbol sintáctico con indentación para mejor legibilidad."""
    from antlr4.tree.Tree import TerminalNode # Importar aquí para asegurar disponibilidad
    
    # Maneja la impresión de terminales (tokens)
    if isinstance(node, TerminalNode):
        return "  " * level + f"TOKEN({node.getText()})"
    
    if node is None or node.getRuleIndex() < 0:
        return "  " * level + f"NODE({type(node).__name__})"

    # Maneja la impresión de reglas (nodos internos)
    rule_name = rule_names[node.getRuleIndex()]
    result = "  " * level + rule_name
    
    for child in node.children or []:
        result += "\n" + pretty_tree(child, rule_names, level + 1)
    return result

# --- FASE 0: CARGA DE DATOS EXTERNOS (CSV) ---
def load_item_properties(symbol_table_instance):
    """Carga propiedades de ítems desde datos_propiedades.csv al SymbolTable."""
    csv_file_path = 'datos_propiedades.csv'
    print(f"--- FASE 0: CARGA DE DATOS ({csv_file_path}) ---")
    try:
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader) # Leer la cabecera
            
            for row in reader:
                if len(row) == 4:
                    nombre = row[1]
                    prop_name = row[2]
                    valor = row[3]
                    symbol_table_instance.add_item_property(nombre, prop_name, valor)
        
        print("✅ Propiedades de ítems cargadas exitosamente al SymbolTable.")
        return True
        
    except FileNotFoundError:
        print(f"❌ ERROR FATAL: Archivo de propiedades '{csv_file_path}' no encontrado.")
        return False
    except Exception as e:
        print(f"❌ ERROR FATAL al procesar CSV: {e}")
        return False

def main():
    try:
        print("--- 1. EJECUCIÓN INICIADA ---")
        
        # ==========================================
        # FASE 0: CARGA DE DATOS
        # ==========================================
        visitor = SceneSemanticVisitor() 
        if not load_item_properties(visitor.symbol_table):
            sys.exit(1)

        # ==========================================
        # FASE 1: ANÁLISIS LÉXICO
        # ==========================================
        input_stream = FileStream("input.txt", encoding='utf-8')
        lexer = GuionesLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(SyntaxErrorListener())

        stream = CommonTokenStream(lexer)
        stream.fill() # Consumir el stream para obtener todos los tokens (FASE 1)
        
        # ==========================================
        # FASE 2: ANÁLISIS SINTÁCTICO
        # ==========================================
        parser = GuionesLangParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())
        
        stream.seek(0) # Reiniciar el stream para que el parser lo procese desde el inicio
        tree = parser.program()

        # --- INICIO DEL REPORTE DETALLADO ---
        print("\n==========================================")
        print("     REPORTE DETALLADO (FASES 1 & 2)      ")
        print("==========================================")
        
        # 1. REPORTE DE TOKENS (FASE 1)
        print("## 🔤 TOKENS")
        visible_token_count = 0
        for token in stream.tokens:
            if token.type != Token.EOF and token.channel == 0:
                visible_token_count += 1
                token_name = parser.symbolicNames[token.type]
                print(f"  {visible_token_count:2d}. {token_name:18} -> '{token.text}' @line {token.line}:{token.column}")
        print(f"Total de tokens significativos: {visible_token_count}")

        # 2. ÁRBOL SINTÁCTICO (toStringTree)
        print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
        print(tree.toStringTree(recog=parser))

        # 3. ÁRBOL SINTÁCTICO (Indentado)
        print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
        print(pretty_tree(tree, parser.ruleNames))
        print("✅ FASES 1 & 2: Reporte detallado completado.")
        # --- FIN DEL REPORTE DETALLADO ---

        # ==========================================
        # FASE 3: ANÁLISIS SEMÁNTICO (Continúa la ejecución)
        # ==========================================
        
        # El Visitor necesita un stream limpio, por lo que es mejor reinstanciar
        # o asegurar que el estado de 'stream' y 'parser' sea consistente.
        # En este caso, ya tenemos el 'visitor' listo con la Tabla de Símbolos cargada.
        
        python_code = visitor.visit(tree) # El Visitor procesa el AST completo

        if visitor.errors:
            print("\n🛑 FASE 3: ERRORES SEMÁNTICOS ENCONTRADOS")
            for error in visitor.errors:
                print(f"  -> {error}")
            sys.exit(1)
        
        print("\n✅ FASE 3: Análisis Semántico completado. Referencias y lógica validadas.")

        # ==========================================
        # FASE 4 & 5: CÓDIGO INTERMEDIO Y FINAL
        # ==========================================
        
        output_file = "output_program.py"
        with open(output_file, "w", encoding='utf-8') as f:
            f.write(python_code)
        
        print(f"\n✅ FASE 4 & 5: Código Python generado en {output_file}.")

        # --- PRUEBA INTERACTIVA MANUAL ---
        print("\n--- PRUEBA INTERACTIVA REQUERIDA ---")
        print("Tu compilador ha finalizado con éxito.")
        print("Para probar la funcionalidad, ejecute manualmente:")
        print(f">>> python3 {output_file}\n")
        print("--------------------------------------")

    except Exception as e:
        print(f"\n❌ ERROR DE COMPILACIÓN DETECTADO: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    # Asegúrate de que la función auxiliar esté definida antes de main()
    from antlr4.tree.Tree import TerminalNode # Esto es necesario para pretty_tree
    main()