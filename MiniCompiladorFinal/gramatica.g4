grammar gramatica;

// Parser rules
program: scene+ EOF ;

scene: ESCENA ID '{' dialogue+ '}' ;

dialogue: DECIR STRING ';'
        | OPCION STRING IR_A ID ';'
        ;

// Lexer rules
ESCENA: 'escena';
DECIR: 'decir';
OPCION: 'opcion';
IR_A: 'ir_a';

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
STRING: '"' (~["\r\n])* '"' ;
WS: [ \t\r\n]+ -> skip ;
