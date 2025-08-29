# Generated from SwitchLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwitchLangParser import SwitchLangParser
else:
    from SwitchLangParser import SwitchLangParser

# This class defines a complete listener for a parse tree produced by SwitchLangParser.
class SwitchLangListener(ParseTreeListener):

    # Enter a parse tree produced by SwitchLangParser#program.
    def enterProgram(self, ctx:SwitchLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#program.
    def exitProgram(self, ctx:SwitchLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#statement.
    def enterStatement(self, ctx:SwitchLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#statement.
    def exitStatement(self, ctx:SwitchLangParser.StatementContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#assignment.
    def enterAssignment(self, ctx:SwitchLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#assignment.
    def exitAssignment(self, ctx:SwitchLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#expr.
    def enterExpr(self, ctx:SwitchLangParser.ExprContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#expr.
    def exitExpr(self, ctx:SwitchLangParser.ExprContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#switchStmt.
    def enterSwitchStmt(self, ctx:SwitchLangParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#switchStmt.
    def exitSwitchStmt(self, ctx:SwitchLangParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#caseBlock.
    def enterCaseBlock(self, ctx:SwitchLangParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#caseBlock.
    def exitCaseBlock(self, ctx:SwitchLangParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#defaultBlock.
    def enterDefaultBlock(self, ctx:SwitchLangParser.DefaultBlockContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#defaultBlock.
    def exitDefaultBlock(self, ctx:SwitchLangParser.DefaultBlockContext):
        pass



del SwitchLangParser