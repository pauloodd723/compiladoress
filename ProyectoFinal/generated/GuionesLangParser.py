# Generated from GuionesLang.g4 by ANTLR 4.13.2
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
        4,1,13,37,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,4,1,18,8,1,11,1,12,1,19,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,2,0,0,3,0,2,4,0,0,37,
        0,7,1,0,0,0,2,13,1,0,0,0,4,34,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,
        9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,
        1,1,0,0,0,13,14,5,1,0,0,14,15,5,6,0,0,15,17,5,9,0,0,16,18,3,4,2,
        0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,
        1,0,0,0,21,22,5,10,0,0,22,3,1,0,0,0,23,24,5,2,0,0,24,25,5,7,0,0,
        25,35,5,11,0,0,26,27,5,3,0,0,27,28,5,7,0,0,28,29,5,4,0,0,29,30,5,
        6,0,0,30,35,5,11,0,0,31,32,5,5,0,0,32,33,5,6,0,0,33,35,5,11,0,0,
        34,23,1,0,0,0,34,26,1,0,0,0,34,31,1,0,0,0,35,5,1,0,0,0,3,9,19,34
    ]

class GuionesLangParser ( Parser ):

    grammarFileName = "GuionesLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'escena'", "'decir'", "'opcion'", "'ir_a'", 
                     "'obtener_item'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "ESCENA", "SAY", "OPTION", "GOTO", "OBTENER_ITEM", 
                      "ID", "STRING", "NUMBER", "LBRACE", "RBRACE", "SEMI", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_scene = 1
    RULE_dialogue = 2

    ruleNames =  [ "program", "scene", "dialogue" ]

    EOF = Token.EOF
    ESCENA=1
    SAY=2
    OPTION=3
    GOTO=4
    OBTENER_ITEM=5
    ID=6
    STRING=7
    NUMBER=8
    LBRACE=9
    RBRACE=10
    SEMI=11
    COMMENT=12
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
            return self.getToken(GuionesLangParser.EOF, 0)

        def scene(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GuionesLangParser.SceneContext)
            else:
                return self.getTypedRuleContext(GuionesLangParser.SceneContext,i)


        def getRuleIndex(self):
            return GuionesLangParser.RULE_program

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

        localctx = GuionesLangParser.ProgramContext(self, self._ctx, self.state)
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
                if not (_la==1):
                    break

            self.state = 11
            self.match(GuionesLangParser.EOF)
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
            return self.getToken(GuionesLangParser.ESCENA, 0)

        def ID(self):
            return self.getToken(GuionesLangParser.ID, 0)

        def LBRACE(self):
            return self.getToken(GuionesLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GuionesLangParser.RBRACE, 0)

        def dialogue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GuionesLangParser.DialogueContext)
            else:
                return self.getTypedRuleContext(GuionesLangParser.DialogueContext,i)


        def getRuleIndex(self):
            return GuionesLangParser.RULE_scene

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

        localctx = GuionesLangParser.SceneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scene)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(GuionesLangParser.ESCENA)
            self.state = 14
            self.match(GuionesLangParser.ID)
            self.state = 15
            self.match(GuionesLangParser.LBRACE)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.dialogue()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 44) != 0)):
                    break

            self.state = 21
            self.match(GuionesLangParser.RBRACE)
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

        def SAY(self):
            return self.getToken(GuionesLangParser.SAY, 0)

        def STRING(self):
            return self.getToken(GuionesLangParser.STRING, 0)

        def SEMI(self):
            return self.getToken(GuionesLangParser.SEMI, 0)

        def OPTION(self):
            return self.getToken(GuionesLangParser.OPTION, 0)

        def GOTO(self):
            return self.getToken(GuionesLangParser.GOTO, 0)

        def ID(self):
            return self.getToken(GuionesLangParser.ID, 0)

        def OBTENER_ITEM(self):
            return self.getToken(GuionesLangParser.OBTENER_ITEM, 0)

        def getRuleIndex(self):
            return GuionesLangParser.RULE_dialogue

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

        localctx = GuionesLangParser.DialogueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dialogue)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(GuionesLangParser.SAY)
                self.state = 24
                self.match(GuionesLangParser.STRING)
                self.state = 25
                self.match(GuionesLangParser.SEMI)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(GuionesLangParser.OPTION)
                self.state = 27
                self.match(GuionesLangParser.STRING)
                self.state = 28
                self.match(GuionesLangParser.GOTO)
                self.state = 29
                self.match(GuionesLangParser.ID)
                self.state = 30
                self.match(GuionesLangParser.SEMI)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(GuionesLangParser.OBTENER_ITEM)
                self.state = 32
                self.match(GuionesLangParser.ID)
                self.state = 33
                self.match(GuionesLangParser.SEMI)
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





