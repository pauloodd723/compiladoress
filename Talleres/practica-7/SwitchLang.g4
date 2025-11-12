grammar SwitchLang;

// 📌 REGLA PRINCIPAL
program     : statement* EOF ;

// 📌 Sentencias
statement   : assignment SEMI
            | switchStmt
            ;

// 📌 Asignación
assignment  : IDENTIFIER EQ expr ;

// 📌 Expresión (solo números o variables para este ejemplo)
expr        : NUMBER
            | IDENTIFIER
            ;

// 📌 Switch
switchStmt  : SWITCH LPAREN expr RPAREN LBRACE caseBlock* defaultBlock? RBRACE ;

// 📌 Bloques de casos
caseBlock   : CASE expr COLON statement* ;
defaultBlock: DEFAULT COLON statement* ;

// 📌 PALABRAS RESERVADAS
SWITCH      : 'switch' ;
CASE        : 'case' ;
DEFAULT     : 'default' ;

// 📌 SÍMBOLOS
LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACE      : '{' ;
RBRACE      : '}' ;
COLON       : ':' ;
SEMI        : ';' ;
EQ          : '=' ;

// 📌 IDENTIFICADORES Y NÚMEROS
IDENTIFIER  : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER      : [0-9]+ ;

// 📌 ESPACIOS Y SALTOS DE LÍNEA
WS          : [ \t\r\n]+ -> skip ;
