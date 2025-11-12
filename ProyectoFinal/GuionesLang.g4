grammar GuionesLang;

// --- REGLAS SINTÁCTICAS (Parser) ---
program    : scene+ EOF ; 
scene      : ESCENA ID LBRACE dialogue+ RBRACE ;

// Reglas de Diálogo (Acciones del juego)
dialogue   : SAY STRING SEMI 
           | OPTION STRING GOTO ID SEMI 
           | OBTENER_ITEM ID SEMI  // Lógica de obtención de Ítem/Pico
           ;

// --- REGLAS LÉXICAS (Lexer) ---
ESCENA       : 'escena' ;
SAY          : 'decir' ;
OPTION       : 'opcion' ;
GOTO         : 'ir_a' ;
OBTENER_ITEM : 'obtener_item' ;

// Palabras clave y literales
ID       : [a-zA-Z_][a-zA-Z_0-9]* ;
STRING   : '"' ('""'|~'"')* '"' ; 
NUMBER   : [0-9]+ ; 

// Símbolos
LBRACE   : '{' ;
RBRACE   : '}' ;
SEMI     : ';' ;

// Ignorar espacios y comentarios
COMMENT  : '//' .*? '\n' -> skip ;
WS       : [ \t\r\n]+ -> skip ;