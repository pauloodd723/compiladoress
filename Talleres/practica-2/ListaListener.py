# Generated from Lista.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ListaParser import ListaParser
else:
    from ListaParser import ListaParser

# This class defines a complete listener for a parse tree produced by ListaParser.
class ListaListener(ParseTreeListener):

    # Enter a parse tree produced by ListaParser#lista.
    def enterLista(self, ctx:ListaParser.ListaContext):
        pass

    # Exit a parse tree produced by ListaParser#lista.
    def exitLista(self, ctx:ListaParser.ListaContext):
        pass


    # Enter a parse tree produced by ListaParser#elementos.
    def enterElementos(self, ctx:ListaParser.ElementosContext):
        pass

    # Exit a parse tree produced by ListaParser#elementos.
    def exitElementos(self, ctx:ListaParser.ElementosContext):
        pass


    # Enter a parse tree produced by ListaParser#elemento.
    def enterElemento(self, ctx:ListaParser.ElementoContext):
        pass

    # Exit a parse tree produced by ListaParser#elemento.
    def exitElemento(self, ctx:ListaParser.ElementoContext):
        pass



del ListaParser