from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
import sys
import subprocess
import os

# --- Importaciones de los módulos del compilador ---
from generated.GuionesLangLexer import GuionesLangLexer
from generated.GuionesLangParser import GuionesLangParser
from semantic_analyzer.SemanticVisitor import SceneSemanticVisitor
from semantic_analyzer.SymbolTable import SymbolTable, SemanticError
from codegen.PythonCodeGenerator import PythonCodeGenerator 

# --- CONFIGURACIÓN DE ERRORES SINTÁCTICOS/LÉXICOS ---
class SyntaxErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error Sintáctico/Léxico en línea {line}:{column}: {msg}")

# --- FUNCIÓN AUXILIAR PARA EL REPORTE (pretty_tree) ---
def pretty_tree(node, rule_names, level=0):
    """Imprime el árbol sintáctico con indentación para mejor legibilidad."""
    from antlr4.tree.Tree import TerminalNode 
    
    if isinstance(node, TerminalNode):
        return "  " * level + f"TOKEN({node.getText()})"
    
    if node is None or node.getRuleIndex() < 0:
        return "  " * level + f"NODE({type(node).__name__})"

    rule_name = rule_names[node.getRuleIndex()]
    result = "  " * level + rule_name
    
    for child in node.children or []:
        result += "\n" + pretty_tree(child, rule_names, level + 1)
    return result

# --- FUNCIÓN DE COMPILACIÓN POR BLOQUE ---
def compile_and_execute_test(test_content, test_id):
    """Compila un único bloque de código fuente y genera un archivo .py."""
    
    # ----------------------------------------------------
    # LÓGICA DEL REPORTE DETALLADO (Solo para la Primera Prueba)
    # ----------------------------------------------------
    show_full_report = (test_id == 1)
    
    if show_full_report:
        print("\n==========================================")
        print("     REPORTE DETALLADO (FASES 1 & 2)      ")
        print("==========================================")
    
    # La Tabla de Símbolos se inicializa para CADA prueba
    symbol_table = SymbolTable() 
    code_generator = PythonCodeGenerator()
    
    # 1. Fases 1 & 2: Análisis Léxico y Sintáctico
    try:
        input_stream = InputStream(test_content)
        lexer = GuionesLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(SyntaxErrorListener())

        stream = CommonTokenStream(lexer)
        stream.fill() # FASE 1: Obtener todos los tokens
        
        parser = GuionesLangParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())
        
        stream.seek(0) # Reiniciar el stream
        tree = parser.program() # FASE 2: Construir el AST

        if show_full_report:
            # --- 1. REPORTE DE TOKENS (FASE 1) ---
            print("## 🔤 TOKENS")
            visible_token_count = 0
            for token in stream.tokens:
                if token.type != Token.EOF and token.channel == 0:
                    visible_token_count += 1
                    token_name = parser.symbolicNames[token.type]
                    print(f"  {visible_token_count:2d}. {token_name:18} -> '{token.text}' @line {token.line}:{token.column}")
            print(f"Total de tokens significativos: {visible_token_count}")

            # --- 2. ÁRBOL SINTÁCTICO (toStringTree) ---
            print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
            print(tree.toStringTree(recog=parser))

            # --- 3. ÁRBOL SINTÁCTICO (Indentado) ---
            print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
            print(pretty_tree(tree, parser.ruleNames))
            print("✅ FASES 1 & 2: Reporte detallado completado.")
        else:
            print("✅ FASES 1 & 2: Análisis Léxico y Sintáctico completado.")
        

    except Exception as e:
        print(f"❌ FASES 1 & 2: Error Léxico/Sintáctico detectado. Deteniendo la compilación para la prueba {test_id}.")
        print(f"   -> {e}")
        return "Léxico/Sintáctico"

    # 2. Fase 3, 4, 5: Análisis Semántico y Generación de Código
    try:
        visitor = SceneSemanticVisitor(symbol_table, code_generator) 
        python_code = visitor.visit(tree)
        
        if visitor.errors:
            print(f"❌ FASE 3: Análisis Semántico fallido para la prueba {test_id}. Errores encontrados:")
            for error in visitor.errors:
                print(f"   -> {error}")
            return "Semántico"
        
        print("✅ FASE 3: Análisis Semántico completado.")

        # Generar Archivo de Salida (Omitido para pruebas de error)
        # output_file = f"output_{test_id}.py"
        # with open(output_file, "w", encoding='utf-8') as f:
        #     f.write(python_code)
            
        # print(f"✅ FASES 4 & 5: Código Python generado en {output_file}.")
        
        return "Éxito"

    except Exception as e:
        print(f"❌ ERROR: Fallo durante la generación para la prueba {test_id}: {e}")
        return "Generación"

# --- LÓGICA PRINCIPAL DE ITERACIÓN ---
def main():
    print("--- 1. EJECUCIÓN MULTI-PRUEBA INICIADA ---")
    
    try:
        # Usamos input.txt para las 10 pruebas válidas
        with open("input.txt", 'r', encoding='utf-8') as f:
            valid_content = f.read()

        test_blocks = valid_content.split('// === PRUEBA ===')
        
        if not test_blocks or (len(test_blocks) == 1 and not test_blocks[0].strip()):
            print("Advertencia: El archivo 'input.txt' está vacío o no tiene bloques de prueba.")
            return

        if not test_blocks[0].strip():
            test_blocks.pop(0)

        print(f"Se detectaron {len(test_blocks)} bloques de prueba válidos para la compilación modular.")

        for i, block in enumerate(test_blocks):
            # Limpiar y asegurar que solo el bloque de código se compile
            compile_and_execute_test(block.strip(), i + 1)
            
        print("\n--- 2. TODAS LAS PRUEBAS VÁLIDAS FINALIZADAS ---")

    except Exception as e:
        print(f"\n❌ ERROR FATAL EN main(): {e}")

if __name__ == '__main__':
    from antlr4.tree.Tree import TerminalNode 
    main()