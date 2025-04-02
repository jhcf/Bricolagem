lexer grammar BricolagemLexer;

options { caseInsensitive = true; }


// Palavras-chave
PROJETO_MAKER: 'ProjetoMaker';
NIVEL: 'Nivel';
TEMA: 'Tema';
OBJETIVO_ENSINO: 'ObjetivoEnsino';
OBJETIVO_APRENDIZAGEM: 'ObjetivoAprendizagem';
OBJETIVO_PESQUISA: 'ObjetivoPesquisa';
OBJETIVO_EDUCACIONAL: 'ObjetivoEducacional';
ATIVIDADES: 'Atividades';
AVALIACAO: 'Avaliacao';
RECURSOS: 'Recursos';
CONFORMIDADE_BNCC: 'ConformidadeBNCC';

// Modificadores
DESCRICAO: 'Descricao';
DURACAOMINUTOS: 'DuracaoMinutos';
PASSOS: 'Passos';
CRITERIOS:    'Criterios';
INSTRUMENTOS: 'Instrumentos';
    
// Símbolos
ABRE_CHAVE: '{';
FECHA_CHAVE: '}';
ABRE_PARENTESE: '(';
FECHA_PARENTESE: ')';
ABRE_COLCHETE: '[';
FECHA_COLCHETE: ']';
DOIS_PONTOS: ':';
VIRGULA: ',';
PONTO_VIRGULA: ';';

// Identificadores e valores
ID: [a-zA-Z_]*[.][a-zA-Z0-9_]*;
NUMERO: [0-9]+;
STRING: '"' .*? '"';

// Ignorar espaços e quebras de linha
WS: [ \t\r\n]+ -> skip;

