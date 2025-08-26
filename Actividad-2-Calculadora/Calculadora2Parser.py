# Generated from Calculadora2.g4 by ANTLR 4.13.2
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
        4,1,11,50,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,3,0,16,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,29,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,40,8,1,10,
        1,12,1,43,9,1,1,2,1,2,1,2,1,2,1,2,1,2,0,1,2,3,0,2,4,0,2,1,0,2,3,
        1,0,4,5,54,0,11,1,0,0,0,2,28,1,0,0,0,4,44,1,0,0,0,6,7,3,2,1,0,7,
        8,5,10,0,0,8,10,1,0,0,0,9,6,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,
        12,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,
        0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,6,
        1,-1,0,20,21,5,5,0,0,21,29,3,2,1,4,22,29,3,4,2,0,23,24,5,6,0,0,24,
        25,3,2,1,0,25,26,5,7,0,0,26,29,1,0,0,0,27,29,5,8,0,0,28,19,1,0,0,
        0,28,22,1,0,0,0,28,23,1,0,0,0,28,27,1,0,0,0,29,41,1,0,0,0,30,31,
        10,7,0,0,31,32,5,1,0,0,32,40,3,2,1,8,33,34,10,6,0,0,34,35,7,0,0,
        0,35,40,3,2,1,7,36,37,10,5,0,0,37,38,7,1,0,0,38,40,3,2,1,6,39,30,
        1,0,0,0,39,33,1,0,0,0,39,36,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,
        41,42,1,0,0,0,42,3,1,0,0,0,43,41,1,0,0,0,44,45,5,9,0,0,45,46,5,6,
        0,0,46,47,3,2,1,0,47,48,5,7,0,0,48,5,1,0,0,0,5,11,15,28,39,41
    ]

class Calculadora2Parser ( Parser ):

    grammarFileName = "Calculadora2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "ID", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_expresion = 1
    RULE_funcion = 2

    ruleNames =  [ "prog", "expresion", "funcion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    ID=9
    NEWLINE=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Calculadora2Parser.EOF, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Calculadora2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(Calculadora2Parser.ExpresionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(Calculadora2Parser.NEWLINE)
            else:
                return self.getToken(Calculadora2Parser.NEWLINE, i)

        def getRuleIndex(self):
            return Calculadora2Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Calculadora2Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 6
                    self.expresion(0)
                    self.state = 7
                    self.match(Calculadora2Parser.NEWLINE) 
                self.state = 13
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 864) != 0):
                self.state = 14
                self.expresion(0)


            self.state = 17
            self.match(Calculadora2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Calculadora2Parser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Calculadora2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(Calculadora2Parser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Calculadora2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Calculadora2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(Calculadora2Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Calculadora2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(Calculadora2Parser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)


    class PotenciaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Calculadora2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Calculadora2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(Calculadora2Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencia" ):
                listener.enterPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencia" ):
                listener.exitPotencia(self)


    class NegativoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Calculadora2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(Calculadora2Parser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativo" ):
                listener.enterNegativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativo" ):
                listener.exitNegativo(self)


    class LlamadaFuncContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Calculadora2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcion(self):
            return self.getTypedRuleContext(Calculadora2Parser.FuncionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFunc" ):
                listener.enterLlamadaFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFunc" ):
                listener.exitLlamadaFunc(self)


    class MultDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Calculadora2Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Calculadora2Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(Calculadora2Parser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDiv" ):
                listener.enterMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDiv" ):
                listener.exitMultDiv(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Calculadora2Parser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = Calculadora2Parser.NegativoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(Calculadora2Parser.T__4)
                self.state = 21
                self.expresion(4)
                pass
            elif token in [9]:
                localctx = Calculadora2Parser.LlamadaFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.funcion()
                pass
            elif token in [6]:
                localctx = Calculadora2Parser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(Calculadora2Parser.T__5)
                self.state = 24
                self.expresion(0)
                self.state = 25
                self.match(Calculadora2Parser.T__6)
                pass
            elif token in [8]:
                localctx = Calculadora2Parser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(Calculadora2Parser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = Calculadora2Parser.PotenciaContext(self, Calculadora2Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 30
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 31
                        self.match(Calculadora2Parser.T__0)
                        self.state = 32
                        self.expresion(8)
                        pass

                    elif la_ == 2:
                        localctx = Calculadora2Parser.MultDivContext(self, Calculadora2Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 33
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 34
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expresion(7)
                        pass

                    elif la_ == 3:
                        localctx = Calculadora2Parser.AddSubContext(self, Calculadora2Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 36
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 37
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        self.expresion(6)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Calculadora2Parser.RULE_funcion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncionSimpleContext(FuncionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Calculadora2Parser.FuncionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Calculadora2Parser.ID, 0)
        def expresion(self):
            return self.getTypedRuleContext(Calculadora2Parser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionSimple" ):
                listener.enterFuncionSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionSimple" ):
                listener.exitFuncionSimple(self)



    def funcion(self):

        localctx = Calculadora2Parser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcion)
        try:
            localctx = Calculadora2Parser.FuncionSimpleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(Calculadora2Parser.ID)
            self.state = 45
            self.match(Calculadora2Parser.T__5)
            self.state = 46
            self.expresion(0)
            self.state = 47
            self.match(Calculadora2Parser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




