import os
import sys
from antlr4 import *
from generated.gramaticaLexer import gramaticaLexer
from generated.gramaticaParser import gramaticaParser
from semantic_analyzer.SemanticAnalyzerVisitor import SemanticAnalyzerVisitor

# --- Configuración ---
INVALID_DIR = "tests/invalid"

# ErrorListener para capturar errores léxicos y sintácticos
from antlr4.error.ErrorListener import ErrorListener

class CaptureErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")

    def reportErrors(self):
        if self.errors:
            raise Exception("\n".join(self.errors))

# Función para correr un archivo inválido
def run_invalid_file(file_path, idx):
    print(f"\n--- Test inválido #{idx}: {os.path.basename(file_path)} ---")
    print("="*50)
    print(f"Archivo: {file_path}")
    print("="*50)

    try:
        input_stream = FileStream(file_path, encoding="utf-8")

        # Lexer
        lexer = gramaticaLexer(input_stream)
        lexer_errors = CaptureErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(lexer_errors)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        # Parser
        parser = gramaticaParser(token_stream)
        parser_errors = CaptureErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(parser_errors)
        tree = parser.program()

        # Revisar errores léxicos y sintácticos
        lexer_errors.reportErrors()
        parser_errors.reportErrors()

        # Análisis semántico
        semantic_visitor = SemanticAnalyzerVisitor()
        semantic_visitor.visit(tree)

        # Si llegamos aquí, no hubo errores (lo cual NO debería pasar)
        print("✅ No se detectó error (esto no debería pasar en un test inválido)")

    except Exception as e:
        print(f"⚠️  Error detectado en este archivo:\n{e}")

    print("-"*50)

# Función principal
def main():
    if not os.path.exists(INVALID_DIR):
        print(f"No se encontró la carpeta: {INVALID_DIR}")
        return

    invalid_files = [f for f in os.listdir(INVALID_DIR) if f.endswith(".txt")]
    invalid_files.sort()  # opcional: ordena por nombre
    print(f"Ejecutando {len(invalid_files)} tests inválidos...")

    for idx, filename in enumerate(invalid_files, start=1):
        file_path = os.path.join(INVALID_DIR, filename)
        run_invalid_file(file_path, idx)

if __name__ == "__main__":
    main()
