grammar Calculadora;

prog: expresion EOF ;

// Reglas de expresión con precedencia
expresion
    : expresion '^' expresion             # Potencia
    | expresion ('*'|'/') expresion       # MultDiv
    | expresion ('+'|'-') expresion       # AddSub
    | '-' expresion                       # Negativo
    | funcion                             # Funcion
    | '(' expresion ')'                   # Parentesis
    | NUMBER                              # Numero
    ;

// Funciones como sqrt(…), abs(…), etc.
funcion
    : ID '(' expresion ')'                # LlamadaFuncion
    ;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
ID     : [a-zA-Z]+ ;
WS     : [ \t\r\n]+ -> skip ;
