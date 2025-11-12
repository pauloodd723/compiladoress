import sys
import os
import subprocess
from antlr4 import *

from generated.gramaticaLexer import gramaticaLexer
from generated.gramaticaParser import gramaticaParser
from semantic_analyzer.SemanticAnalyzerVisitor import SemanticAnalyzerVisitor
from codegen.PythonCodeGenerator import PythonCodeGenerator

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo_dialogo.txt>")
        return

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: no se encontró el archivo {input_file}")
        return

    base_name = os.path.basename(input_file)
    name_without_ext = os.path.splitext(base_name)[0]

    # Crear carpeta output si no existe
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{name_without_ext}.py")

    print("="*50)
    print(f"🚀 MiniCompilador Minecraft 🚀")
    print(f"Entrada: {input_file}")
    print(f"Salida:  {output_file}")
    print("="*50)

   # --- Análisis léxico ---
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = gramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("\n--- Tokens ---")
    for token in token_stream.tokens:
        if token.type == Token.EOF:
            token_name = "EOF"
        elif 0 < token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] not in [None, "<INVALID>"]:
            token_name = lexer.symbolicNames[token.type]
        elif 0 < token.type < len(lexer.literalNames) and lexer.literalNames[token.type] not in [None, "<INVALID>"]:
            token_name = lexer.literalNames[token.type].strip("'")
        else:
            continue  # saltar tokens desconocidos
        print(f"{token.text} -> {token_name}")
    # --- Análisis sintáctico ---
    parser = gramaticaParser(token_stream)
    tree = parser.program()
    print("\n--- Árbol Sintáctico ---")
    print(tree.toStringTree(recog=parser))
    print("[OK] Análisis léxico y sintáctico exitoso.")

    # --- Análisis semántico ---
    semantic_visitor = SemanticAnalyzerVisitor()
    ir = semantic_visitor.visit(tree)
    print("[OK] Análisis semántico exitoso.")

    # --- Generación de Python ---
    py_gen = PythonCodeGenerator(ir.instructions)
    python_code = py_gen.generate()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(python_code)
    print(f"[OK] Código Python generado en: {output_file}")

    # --- Ejecutar script generado ---
    print("\n--- Ejecutando el script generado ---")
    subprocess.run([sys.executable, output_file])

if __name__ == "__main__":
    main()
