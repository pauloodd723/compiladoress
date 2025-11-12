from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser

# Entrada de prueba con if-else
input_text = "if (x > 10) { y = y + 1; } else { y = y - 1; };"

# Crear flujo de entrada
input_stream = InputStream(input_text)

# Crear analizador léxico y parser
lexer = MiGramaticaLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = MiGramaticaParser(token_stream)

# Analizar la entrada
tree = parser.programa()

# Mostrar el árbol de análisis sintáctico
print(tree.toStringTree(recog=parser))