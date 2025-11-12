# Generated from gramatica.g4 by ANTLR 4.13.2
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
        4,1,10,34,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,4,1,18,8,1,11,1,12,1,19,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,32,8,2,1,2,0,0,3,0,2,4,0,0,33,0,7,1,0,0,
        0,2,13,1,0,0,0,4,31,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,
        9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,
        0,13,14,5,4,0,0,14,15,5,8,0,0,15,17,5,1,0,0,16,18,3,4,2,0,17,16,
        1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,
        21,22,5,2,0,0,22,3,1,0,0,0,23,24,5,5,0,0,24,25,5,9,0,0,25,32,5,3,
        0,0,26,27,5,6,0,0,27,28,5,9,0,0,28,29,5,7,0,0,29,30,5,8,0,0,30,32,
        5,3,0,0,31,23,1,0,0,0,31,26,1,0,0,0,32,5,1,0,0,0,3,9,19,31
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'escena'", "'decir'", 
                     "'opcion'", "'ir_a'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ESCENA", "DECIR", "OPCION", "IR_A", "ID", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_scene = 1
    RULE_dialogue = 2

    ruleNames =  [ "program", "scene", "dialogue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ESCENA=4
    DECIR=5
    OPCION=6
    IR_A=7
    ID=8
    STRING=9
    WS=10

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
            return self.getToken(gramaticaParser.EOF, 0)

        def scene(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SceneContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SceneContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.scene()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 11
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SceneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCENA(self):
            return self.getToken(gramaticaParser.ESCENA, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def dialogue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DialogueContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DialogueContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_scene

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScene" ):
                listener.enterScene(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScene" ):
                listener.exitScene(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScene" ):
                return visitor.visitScene(self)
            else:
                return visitor.visitChildren(self)




    def scene(self):

        localctx = gramaticaParser.SceneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scene)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(gramaticaParser.ESCENA)
            self.state = 14
            self.match(gramaticaParser.ID)
            self.state = 15
            self.match(gramaticaParser.T__0)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.dialogue()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==6):
                    break

            self.state = 21
            self.match(gramaticaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DialogueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIR(self):
            return self.getToken(gramaticaParser.DECIR, 0)

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def OPCION(self):
            return self.getToken(gramaticaParser.OPCION, 0)

        def IR_A(self):
            return self.getToken(gramaticaParser.IR_A, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_dialogue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDialogue" ):
                listener.enterDialogue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDialogue" ):
                listener.exitDialogue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDialogue" ):
                return visitor.visitDialogue(self)
            else:
                return visitor.visitChildren(self)




    def dialogue(self):

        localctx = gramaticaParser.DialogueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dialogue)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(gramaticaParser.DECIR)
                self.state = 24
                self.match(gramaticaParser.STRING)
                self.state = 25
                self.match(gramaticaParser.T__2)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(gramaticaParser.OPCION)
                self.state = 27
                self.match(gramaticaParser.STRING)
                self.state = 28
                self.match(gramaticaParser.IR_A)
                self.state = 29
                self.match(gramaticaParser.ID)
                self.state = 30
                self.match(gramaticaParser.T__2)
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





