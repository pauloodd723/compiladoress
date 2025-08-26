grammar Calculadora2;

prog
    : (expresion NEWLINE)* expresion? EOF
    ;

// Reglas de expresión con precedencia
expresion
    : expresion '^' expresion             # Potencia
    | expresion ('*'|'/') expresion       # MultDiv
    | expresion ('+'|'-') expresion       # AddSub
    | '-' expresion                       # Negativo
    | funcion                             # LlamadaFunc
    | '(' expresion ')'                   # Parentesis
    | NUMBER                              # Numero
    ;

funcion
    : ID '(' expresion ')'                # FuncionSimple
    ;

// Tokens
NUMBER  : [0-9]+ ('.' [0-9]+)? ;
ID      : [a-zA-Z]+ ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;
