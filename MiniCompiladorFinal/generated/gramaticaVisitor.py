# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#program.
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#scene.
    def visitScene(self, ctx:gramaticaParser.SceneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#dialogue.
    def visitDialogue(self, ctx:gramaticaParser.DialogueContext):
        return self.visitChildren(ctx)



del gramaticaParser