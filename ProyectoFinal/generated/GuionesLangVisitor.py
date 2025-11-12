# Generated from GuionesLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GuionesLangParser import GuionesLangParser
else:
    from GuionesLangParser import GuionesLangParser

# This class defines a complete generic visitor for a parse tree produced by GuionesLangParser.

class GuionesLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GuionesLangParser#program.
    def visitProgram(self, ctx:GuionesLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuionesLangParser#scene.
    def visitScene(self, ctx:GuionesLangParser.SceneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuionesLangParser#dialogue.
    def visitDialogue(self, ctx:GuionesLangParser.DialogueContext):
        return self.visitChildren(ctx)



del GuionesLangParser