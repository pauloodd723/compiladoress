# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#scene.
    def enterScene(self, ctx:gramaticaParser.SceneContext):
        pass

    # Exit a parse tree produced by gramaticaParser#scene.
    def exitScene(self, ctx:gramaticaParser.SceneContext):
        pass


    # Enter a parse tree produced by gramaticaParser#dialogue.
    def enterDialogue(self, ctx:gramaticaParser.DialogueContext):
        pass

    # Exit a parse tree produced by gramaticaParser#dialogue.
    def exitDialogue(self, ctx:gramaticaParser.DialogueContext):
        pass



del gramaticaParser