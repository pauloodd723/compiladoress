# Generated from SwitchLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,41,8,4,10,
        4,12,4,44,9,4,1,4,3,4,47,8,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,55,8,5,
        10,5,12,5,58,9,5,1,6,1,6,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,6,0,0,
        7,0,2,4,6,8,10,12,0,1,1,0,11,12,66,0,17,1,0,0,0,2,26,1,0,0,0,4,28,
        1,0,0,0,6,32,1,0,0,0,8,34,1,0,0,0,10,50,1,0,0,0,12,59,1,0,0,0,14,
        16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,
        0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,3,
        4,2,0,23,24,5,9,0,0,24,27,1,0,0,0,25,27,3,8,4,0,26,22,1,0,0,0,26,
        25,1,0,0,0,27,3,1,0,0,0,28,29,5,11,0,0,29,30,5,10,0,0,30,31,3,6,
        3,0,31,5,1,0,0,0,32,33,7,0,0,0,33,7,1,0,0,0,34,35,5,1,0,0,35,36,
        5,4,0,0,36,37,3,6,3,0,37,38,5,5,0,0,38,42,5,6,0,0,39,41,3,10,5,0,
        40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,46,1,
        0,0,0,44,42,1,0,0,0,45,47,3,12,6,0,46,45,1,0,0,0,46,47,1,0,0,0,47,
        48,1,0,0,0,48,49,5,7,0,0,49,9,1,0,0,0,50,51,5,2,0,0,51,52,3,6,3,
        0,52,56,5,8,0,0,53,55,3,2,1,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,
        1,0,0,0,56,57,1,0,0,0,57,11,1,0,0,0,58,56,1,0,0,0,59,60,5,3,0,0,
        60,64,5,8,0,0,61,63,3,2,1,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,
        0,0,0,64,65,1,0,0,0,65,13,1,0,0,0,66,64,1,0,0,0,6,17,26,42,46,56,
        64
    ]

class SwitchLangParser ( Parser ):

    grammarFileName = "SwitchLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'switch'", "'case'", "'default'", "'('", 
                     "')'", "'{'", "'}'", "':'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "SWITCH", "CASE", "DEFAULT", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "COLON", "SEMI", "EQ", 
                      "IDENTIFIER", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expr = 3
    RULE_switchStmt = 4
    RULE_caseBlock = 5
    RULE_defaultBlock = 6

    ruleNames =  [ "program", "statement", "assignment", "expr", "switchStmt", 
                   "caseBlock", "defaultBlock" ]

    EOF = Token.EOF
    SWITCH=1
    CASE=2
    DEFAULT=3
    LPAREN=4
    RPAREN=5
    LBRACE=6
    RBRACE=7
    COLON=8
    SEMI=9
    EQ=10
    IDENTIFIER=11
    NUMBER=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SwitchLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SwitchLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==11:
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(SwitchLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(SwitchLangParser.AssignmentContext,0)


        def SEMI(self):
            return self.getToken(SwitchLangParser.SEMI, 0)

        def switchStmt(self):
            return self.getTypedRuleContext(SwitchLangParser.SwitchStmtContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SwitchLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.assignment()
                self.state = 23
                self.match(SwitchLangParser.SEMI)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.switchStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SwitchLangParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(SwitchLangParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(SwitchLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = SwitchLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(SwitchLangParser.IDENTIFIER)
            self.state = 29
            self.match(SwitchLangParser.EQ)
            self.state = 30
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SwitchLangParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(SwitchLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = SwitchLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(SwitchLangParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(SwitchLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwitchLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SwitchLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(SwitchLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SwitchLangParser.RBRACE, 0)

        def caseBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.CaseBlockContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.CaseBlockContext,i)


        def defaultBlock(self):
            return self.getTypedRuleContext(SwitchLangParser.DefaultBlockContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)




    def switchStmt(self):

        localctx = SwitchLangParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(SwitchLangParser.SWITCH)
            self.state = 35
            self.match(SwitchLangParser.LPAREN)
            self.state = 36
            self.expr()
            self.state = 37
            self.match(SwitchLangParser.RPAREN)
            self.state = 38
            self.match(SwitchLangParser.LBRACE)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 39
                self.caseBlock()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 45
                self.defaultBlock()


            self.state = 48
            self.match(SwitchLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(SwitchLangParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(SwitchLangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(SwitchLangParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_caseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseBlock" ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseBlock" ):
                listener.exitCaseBlock(self)




    def caseBlock(self):

        localctx = SwitchLangParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(SwitchLangParser.CASE)
            self.state = 51
            self.expr()
            self.state = 52
            self.match(SwitchLangParser.COLON)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==11:
                self.state = 53
                self.statement()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(SwitchLangParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(SwitchLangParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_defaultBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultBlock" ):
                listener.enterDefaultBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultBlock" ):
                listener.exitDefaultBlock(self)




    def defaultBlock(self):

        localctx = SwitchLangParser.DefaultBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_defaultBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(SwitchLangParser.DEFAULT)
            self.state = 60
            self.match(SwitchLangParser.COLON)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==11:
                self.state = 61
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





