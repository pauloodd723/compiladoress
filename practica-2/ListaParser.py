# Generated from Lista.g4 by ANTLR 4.13.2
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
        4,1,6,23,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,0,1,0,1,1,1,
        1,1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,
        0,4,5,21,0,6,1,0,0,0,2,12,1,0,0,0,4,20,1,0,0,0,6,8,5,1,0,0,7,9,3,
        2,1,0,8,7,1,0,0,0,8,9,1,0,0,0,9,10,1,0,0,0,10,11,5,2,0,0,11,1,1,
        0,0,0,12,17,3,4,2,0,13,14,5,3,0,0,14,16,3,4,2,0,15,13,1,0,0,0,16,
        19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,3,1,0,0,0,19,17,1,0,0,
        0,20,21,7,0,0,0,21,5,1,0,0,0,2,8,17
    ]

class ListaParser ( Parser ):

    grammarFileName = "Lista.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "STRING", "WS" ]

    RULE_lista = 0
    RULE_elementos = 1
    RULE_elemento = 2

    ruleNames =  [ "lista", "elementos", "elemento" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUMBER=4
    STRING=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementos(self):
            return self.getTypedRuleContext(ListaParser.ElementosContext,0)


        def getRuleIndex(self):
            return ListaParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)




    def lista(self):

        localctx = ListaParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(ListaParser.T__0)
            self.state = 8
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==5:
                self.state = 7
                self.elementos()


            self.state = 10
            self.match(ListaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListaParser.ElementoContext)
            else:
                return self.getTypedRuleContext(ListaParser.ElementoContext,i)


        def getRuleIndex(self):
            return ListaParser.RULE_elementos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementos" ):
                listener.enterElementos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementos" ):
                listener.exitElementos(self)




    def elementos(self):

        localctx = ListaParser.ElementosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_elementos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.elemento()
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 13
                self.match(ListaParser.T__2)
                self.state = 14
                self.elemento()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ListaParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ListaParser.STRING, 0)

        def getRuleIndex(self):
            return ListaParser.RULE_elemento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemento" ):
                listener.enterElemento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemento" ):
                listener.exitElemento(self)




    def elemento(self):

        localctx = ListaParser.ElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_elemento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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





