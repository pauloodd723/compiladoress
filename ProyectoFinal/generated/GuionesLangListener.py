# Generated from GuionesLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GuionesLangParser import GuionesLangParser
else:
    from GuionesLangParser import GuionesLangParser

# This class defines a complete listener for a parse tree produced by GuionesLangParser.
class GuionesLangListener(ParseTreeListener):

    # Enter a parse tree produced by GuionesLangParser#program.
    def enterProgram(self, ctx:GuionesLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by GuionesLangParser#program.
    def exitProgram(self, ctx:GuionesLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by GuionesLangParser#scene.
    def enterScene(self, ctx:GuionesLangParser.SceneContext):
        pass

    # Exit a parse tree produced by GuionesLangParser#scene.
    def exitScene(self, ctx:GuionesLangParser.SceneContext):
        pass


    # Enter a parse tree produced by GuionesLangParser#dialogue.
    def enterDialogue(self, ctx:GuionesLangParser.DialogueContext):
        pass

    # Exit a parse tree produced by GuionesLangParser#dialogue.
    def exitDialogue(self, ctx:GuionesLangParser.DialogueContext):
        pass



del GuionesLangParser