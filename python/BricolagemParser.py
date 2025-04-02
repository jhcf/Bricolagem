# Generated from BricolagemParser.g4 by ANTLR 4.13.2
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
        4,1,29,367,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,0,1,0,1,0,1,1,
        1,1,1,1,5,1,97,8,1,10,1,12,1,100,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,109,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,122,
        8,5,10,5,12,5,125,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,151,8,
        6,1,7,1,7,1,7,5,7,156,8,7,10,7,12,7,159,9,7,3,7,161,8,7,1,8,1,8,
        1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,5,11,174,8,11,10,11,12,
        11,177,9,11,3,11,179,8,11,1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,
        1,15,1,15,1,15,5,15,192,8,15,10,15,12,15,195,9,15,3,15,197,8,15,
        1,16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,5,19,210,
        8,19,10,19,12,19,213,9,19,3,19,215,8,19,1,20,1,20,1,20,1,20,1,21,
        1,21,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,5,24,
        234,8,24,10,24,12,24,237,9,24,3,24,239,8,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,26,1,26,1,27,1,27,1,27,5,27,252,8,27,10,27,12,27,255,
        9,27,3,27,257,8,27,1,28,1,28,1,28,3,28,262,8,28,1,29,1,29,1,29,1,
        29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,278,8,
        31,10,31,12,31,281,9,31,1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,33,
        1,33,1,33,1,34,1,34,1,34,5,34,296,8,34,10,34,12,34,299,9,34,3,34,
        301,8,34,1,35,1,35,3,35,305,8,35,1,36,1,36,1,36,1,36,1,36,1,36,5,
        36,313,8,36,10,36,12,36,316,9,36,1,36,1,36,1,37,1,37,1,38,1,38,1,
        38,1,38,1,38,1,38,5,38,328,8,38,10,38,12,38,331,9,38,1,38,1,38,1,
        39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,5,40,343,8,40,10,40,12,40,
        346,9,40,1,40,1,40,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,5,42,
        358,8,42,10,42,12,42,361,9,42,1,42,1,42,1,43,1,43,1,43,0,0,44,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,0,0,
        355,0,88,1,0,0,0,2,93,1,0,0,0,4,108,1,0,0,0,6,110,1,0,0,0,8,114,
        1,0,0,0,10,118,1,0,0,0,12,150,1,0,0,0,14,160,1,0,0,0,16,162,1,0,
        0,0,18,166,1,0,0,0,20,168,1,0,0,0,22,178,1,0,0,0,24,180,1,0,0,0,
        26,184,1,0,0,0,28,186,1,0,0,0,30,196,1,0,0,0,32,198,1,0,0,0,34,202,
        1,0,0,0,36,204,1,0,0,0,38,214,1,0,0,0,40,216,1,0,0,0,42,220,1,0,
        0,0,44,222,1,0,0,0,46,224,1,0,0,0,48,238,1,0,0,0,50,240,1,0,0,0,
        52,246,1,0,0,0,54,256,1,0,0,0,56,261,1,0,0,0,58,263,1,0,0,0,60,267,
        1,0,0,0,62,271,1,0,0,0,64,284,1,0,0,0,66,286,1,0,0,0,68,300,1,0,
        0,0,70,304,1,0,0,0,72,306,1,0,0,0,74,319,1,0,0,0,76,321,1,0,0,0,
        78,334,1,0,0,0,80,336,1,0,0,0,82,349,1,0,0,0,84,351,1,0,0,0,86,364,
        1,0,0,0,88,89,5,1,0,0,89,90,5,21,0,0,90,91,3,2,1,0,91,92,5,22,0,
        0,92,1,1,0,0,0,93,98,3,4,2,0,94,95,5,24,0,0,95,97,3,4,2,0,96,94,
        1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,3,1,0,0,0,
        100,98,1,0,0,0,101,109,3,6,3,0,102,109,3,8,4,0,103,109,3,10,5,0,
        104,109,3,46,23,0,105,109,3,66,33,0,106,109,3,80,40,0,107,109,3,
        84,42,0,108,101,1,0,0,0,108,102,1,0,0,0,108,103,1,0,0,0,108,104,
        1,0,0,0,108,105,1,0,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,5,1,
        0,0,0,110,111,5,2,0,0,111,112,5,23,0,0,112,113,5,28,0,0,113,7,1,
        0,0,0,114,115,5,3,0,0,115,116,5,23,0,0,116,117,5,28,0,0,117,9,1,
        0,0,0,118,123,3,12,6,0,119,120,5,24,0,0,120,122,3,12,6,0,121,119,
        1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,11,1,
        0,0,0,125,123,1,0,0,0,126,127,5,4,0,0,127,128,5,23,0,0,128,129,5,
        21,0,0,129,130,3,14,7,0,130,131,5,22,0,0,131,151,1,0,0,0,132,133,
        5,5,0,0,133,134,5,23,0,0,134,135,5,21,0,0,135,136,3,22,11,0,136,
        137,5,22,0,0,137,151,1,0,0,0,138,139,5,6,0,0,139,140,5,23,0,0,140,
        141,5,21,0,0,141,142,3,30,15,0,142,143,5,22,0,0,143,151,1,0,0,0,
        144,145,5,7,0,0,145,146,5,23,0,0,146,147,5,21,0,0,147,148,3,38,19,
        0,148,149,5,22,0,0,149,151,1,0,0,0,150,126,1,0,0,0,150,132,1,0,0,
        0,150,138,1,0,0,0,150,144,1,0,0,0,151,13,1,0,0,0,152,157,3,16,8,
        0,153,154,5,24,0,0,154,156,3,16,8,0,155,153,1,0,0,0,156,159,1,0,
        0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,161,1,0,0,0,159,157,1,0,
        0,0,160,152,1,0,0,0,160,161,1,0,0,0,161,15,1,0,0,0,162,163,3,18,
        9,0,163,164,5,23,0,0,164,165,3,20,10,0,165,17,1,0,0,0,166,167,5,
        26,0,0,167,19,1,0,0,0,168,169,5,28,0,0,169,21,1,0,0,0,170,175,3,
        24,12,0,171,172,5,24,0,0,172,174,3,24,12,0,173,171,1,0,0,0,174,177,
        1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,179,1,0,0,0,177,175,
        1,0,0,0,178,170,1,0,0,0,178,179,1,0,0,0,179,23,1,0,0,0,180,181,3,
        26,13,0,181,182,5,23,0,0,182,183,3,28,14,0,183,25,1,0,0,0,184,185,
        5,26,0,0,185,27,1,0,0,0,186,187,5,28,0,0,187,29,1,0,0,0,188,193,
        3,32,16,0,189,190,5,24,0,0,190,192,3,32,16,0,191,189,1,0,0,0,192,
        195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,197,1,0,0,0,195,
        193,1,0,0,0,196,188,1,0,0,0,196,197,1,0,0,0,197,31,1,0,0,0,198,199,
        3,34,17,0,199,200,5,23,0,0,200,201,3,36,18,0,201,33,1,0,0,0,202,
        203,5,26,0,0,203,35,1,0,0,0,204,205,5,28,0,0,205,37,1,0,0,0,206,
        211,3,40,20,0,207,208,5,24,0,0,208,210,3,40,20,0,209,207,1,0,0,0,
        210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,215,1,0,0,0,
        213,211,1,0,0,0,214,206,1,0,0,0,214,215,1,0,0,0,215,39,1,0,0,0,216,
        217,3,42,21,0,217,218,5,23,0,0,218,219,3,44,22,0,219,41,1,0,0,0,
        220,221,5,26,0,0,221,43,1,0,0,0,222,223,5,28,0,0,223,45,1,0,0,0,
        224,225,5,8,0,0,225,226,5,23,0,0,226,227,5,21,0,0,227,228,3,48,24,
        0,228,229,5,22,0,0,229,47,1,0,0,0,230,235,3,50,25,0,231,232,5,24,
        0,0,232,234,3,50,25,0,233,231,1,0,0,0,234,237,1,0,0,0,235,233,1,
        0,0,0,235,236,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,238,230,1,
        0,0,0,238,239,1,0,0,0,239,49,1,0,0,0,240,241,3,52,26,0,241,242,5,
        23,0,0,242,243,5,21,0,0,243,244,3,54,27,0,244,245,5,22,0,0,245,51,
        1,0,0,0,246,247,5,28,0,0,247,53,1,0,0,0,248,253,3,56,28,0,249,250,
        5,24,0,0,250,252,3,56,28,0,251,249,1,0,0,0,252,255,1,0,0,0,253,251,
        1,0,0,0,253,254,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,256,248,
        1,0,0,0,256,257,1,0,0,0,257,55,1,0,0,0,258,262,3,58,29,0,259,262,
        3,60,30,0,260,262,3,62,31,0,261,258,1,0,0,0,261,259,1,0,0,0,261,
        260,1,0,0,0,262,57,1,0,0,0,263,264,5,12,0,0,264,265,5,23,0,0,265,
        266,5,28,0,0,266,59,1,0,0,0,267,268,5,13,0,0,268,269,5,23,0,0,269,
        270,5,27,0,0,270,61,1,0,0,0,271,272,5,14,0,0,272,273,5,23,0,0,273,
        274,5,21,0,0,274,279,3,64,32,0,275,276,5,24,0,0,276,278,3,64,32,
        0,277,275,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,
        0,280,282,1,0,0,0,281,279,1,0,0,0,282,283,5,22,0,0,283,63,1,0,0,
        0,284,285,5,28,0,0,285,65,1,0,0,0,286,287,5,9,0,0,287,288,5,23,0,
        0,288,289,5,21,0,0,289,290,3,68,34,0,290,291,5,22,0,0,291,67,1,0,
        0,0,292,297,3,70,35,0,293,294,5,24,0,0,294,296,3,70,35,0,295,293,
        1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,301,
        1,0,0,0,299,297,1,0,0,0,300,292,1,0,0,0,300,301,1,0,0,0,301,69,1,
        0,0,0,302,305,3,72,36,0,303,305,3,76,38,0,304,302,1,0,0,0,304,303,
        1,0,0,0,305,71,1,0,0,0,306,307,5,15,0,0,307,308,5,23,0,0,308,309,
        5,21,0,0,309,314,3,74,37,0,310,311,5,24,0,0,311,313,3,74,37,0,312,
        310,1,0,0,0,313,316,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,315,
        317,1,0,0,0,316,314,1,0,0,0,317,318,5,22,0,0,318,73,1,0,0,0,319,
        320,5,28,0,0,320,75,1,0,0,0,321,322,5,16,0,0,322,323,5,23,0,0,323,
        324,5,21,0,0,324,329,3,78,39,0,325,326,5,24,0,0,326,328,3,78,39,
        0,327,325,1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,1,0,0,
        0,330,332,1,0,0,0,331,329,1,0,0,0,332,333,5,22,0,0,333,77,1,0,0,
        0,334,335,5,28,0,0,335,79,1,0,0,0,336,337,5,10,0,0,337,338,5,23,
        0,0,338,339,5,21,0,0,339,344,3,82,41,0,340,341,5,24,0,0,341,343,
        3,82,41,0,342,340,1,0,0,0,343,346,1,0,0,0,344,342,1,0,0,0,344,345,
        1,0,0,0,345,347,1,0,0,0,346,344,1,0,0,0,347,348,5,22,0,0,348,81,
        1,0,0,0,349,350,5,28,0,0,350,83,1,0,0,0,351,352,5,11,0,0,352,353,
        5,23,0,0,353,354,5,21,0,0,354,359,3,86,43,0,355,356,5,24,0,0,356,
        358,3,86,43,0,357,355,1,0,0,0,358,361,1,0,0,0,359,357,1,0,0,0,359,
        360,1,0,0,0,360,362,1,0,0,0,361,359,1,0,0,0,362,363,5,22,0,0,363,
        85,1,0,0,0,364,365,5,26,0,0,365,87,1,0,0,0,25,98,108,123,150,157,
        160,175,178,193,196,211,214,235,238,253,256,261,279,297,300,304,
        314,329,344,359
    ]

class BricolagemParser ( Parser ):

    grammarFileName = "BricolagemParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ProjetoMaker'", "'Nivel'", "'Tema'", 
                     "'ObjetivoEnsino'", "'ObjetivoAprendizagem'", "'ObjetivoPesquisa'", 
                     "'ObjetivoEducacional'", "'Atividades'", "'Avaliacao'", 
                     "'Recursos'", "'ConformidadeBNCC'", "'Descricao'", 
                     "'DuracaoMinutos'", "'Passos'", "'Criterios'", "'Instrumentos'", 
                     "'{'", "'}'", "'('", "')'", "'['", "']'", "':'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "PROJETO_MAKER", "NIVEL", "TEMA", "OBJETIVO_ENSINO", 
                      "OBJETIVO_APRENDIZAGEM", "OBJETIVO_PESQUISA", "OBJETIVO_EDUCACIONAL", 
                      "ATIVIDADES", "AVALIACAO", "RECURSOS", "CONFORMIDADE_BNCC", 
                      "DESCRICAO", "DURACAOMINUTOS", "PASSOS", "CRITERIOS", 
                      "INSTRUMENTOS", "ABRE_CHAVE", "FECHA_CHAVE", "ABRE_PARENTESE", 
                      "FECHA_PARENTESE", "ABRE_COLCHETE", "FECHA_COLCHETE", 
                      "DOIS_PONTOS", "VIRGULA", "PONTO_VIRGULA", "ID", "NUMERO", 
                      "STRING", "WS" ]

    RULE_projetoMaker = 0
    RULE_listaElementos = 1
    RULE_elemento = 2
    RULE_nivel = 3
    RULE_tema = 4
    RULE_objetivosProjeto = 5
    RULE_objetivo = 6
    RULE_listaObjetivosEnsino = 7
    RULE_objetivoEnsino = 8
    RULE_idObjetivoEnsino = 9
    RULE_descricaoObjetivoEnsino = 10
    RULE_listaObjetivosAprendizagem = 11
    RULE_objetivoAprendizagem = 12
    RULE_idObjetivoAprendizagem = 13
    RULE_descricaoObjetivoAprendizagem = 14
    RULE_listaObjetivosPesquisa = 15
    RULE_objetivoPesquisa = 16
    RULE_idObjetivoPesquisa = 17
    RULE_descricaoObjetivoPesquisa = 18
    RULE_listaObjetivosEducacionais = 19
    RULE_objetivoEducacional = 20
    RULE_idObjetivoEducacional = 21
    RULE_descricaoObjetivoEducacional = 22
    RULE_atividadesProjeto = 23
    RULE_listaAtividades = 24
    RULE_atividade = 25
    RULE_nomeAtividade = 26
    RULE_listaComponentesAtividade = 27
    RULE_componenteAtividade = 28
    RULE_descricaoAtividade = 29
    RULE_duracaoAtividade = 30
    RULE_passosAtividade = 31
    RULE_passoAtividade = 32
    RULE_avaliacaoProjeto = 33
    RULE_listaComponentesAvaliacao = 34
    RULE_componenteAvaliacao = 35
    RULE_criteriosAvaliacao = 36
    RULE_criterioAvaliacao = 37
    RULE_instrumentosAvaliacao = 38
    RULE_instrumentoAvaliacao = 39
    RULE_recursosProjeto = 40
    RULE_recurso = 41
    RULE_conformidadeProjetoBNCC = 42
    RULE_idBNCC = 43

    ruleNames =  [ "projetoMaker", "listaElementos", "elemento", "nivel", 
                   "tema", "objetivosProjeto", "objetivo", "listaObjetivosEnsino", 
                   "objetivoEnsino", "idObjetivoEnsino", "descricaoObjetivoEnsino", 
                   "listaObjetivosAprendizagem", "objetivoAprendizagem", 
                   "idObjetivoAprendizagem", "descricaoObjetivoAprendizagem", 
                   "listaObjetivosPesquisa", "objetivoPesquisa", "idObjetivoPesquisa", 
                   "descricaoObjetivoPesquisa", "listaObjetivosEducacionais", 
                   "objetivoEducacional", "idObjetivoEducacional", "descricaoObjetivoEducacional", 
                   "atividadesProjeto", "listaAtividades", "atividade", 
                   "nomeAtividade", "listaComponentesAtividade", "componenteAtividade", 
                   "descricaoAtividade", "duracaoAtividade", "passosAtividade", 
                   "passoAtividade", "avaliacaoProjeto", "listaComponentesAvaliacao", 
                   "componenteAvaliacao", "criteriosAvaliacao", "criterioAvaliacao", 
                   "instrumentosAvaliacao", "instrumentoAvaliacao", "recursosProjeto", 
                   "recurso", "conformidadeProjetoBNCC", "idBNCC" ]

    EOF = Token.EOF
    PROJETO_MAKER=1
    NIVEL=2
    TEMA=3
    OBJETIVO_ENSINO=4
    OBJETIVO_APRENDIZAGEM=5
    OBJETIVO_PESQUISA=6
    OBJETIVO_EDUCACIONAL=7
    ATIVIDADES=8
    AVALIACAO=9
    RECURSOS=10
    CONFORMIDADE_BNCC=11
    DESCRICAO=12
    DURACAOMINUTOS=13
    PASSOS=14
    CRITERIOS=15
    INSTRUMENTOS=16
    ABRE_CHAVE=17
    FECHA_CHAVE=18
    ABRE_PARENTESE=19
    FECHA_PARENTESE=20
    ABRE_COLCHETE=21
    FECHA_COLCHETE=22
    DOIS_PONTOS=23
    VIRGULA=24
    PONTO_VIRGULA=25
    ID=26
    NUMERO=27
    STRING=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProjetoMakerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROJETO_MAKER(self):
            return self.getToken(BricolagemParser.PROJETO_MAKER, 0)

        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)

        def listaElementos(self):
            return self.getTypedRuleContext(BricolagemParser.ListaElementosContext,0)


        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_projetoMaker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProjetoMaker" ):
                listener.enterProjetoMaker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProjetoMaker" ):
                listener.exitProjetoMaker(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProjetoMaker" ):
                return visitor.visitProjetoMaker(self)
            else:
                return visitor.visitChildren(self)




    def projetoMaker(self):

        localctx = BricolagemParser.ProjetoMakerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_projetoMaker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(BricolagemParser.PROJETO_MAKER)
            self.state = 89
            self.match(BricolagemParser.ABRE_COLCHETE)
            self.state = 90
            self.listaElementos()
            self.state = 91
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaElementosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.ElementoContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.ElementoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_listaElementos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaElementos" ):
                listener.enterListaElementos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaElementos" ):
                listener.exitListaElementos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaElementos" ):
                return visitor.visitListaElementos(self)
            else:
                return visitor.visitChildren(self)




    def listaElementos(self):

        localctx = BricolagemParser.ListaElementosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_listaElementos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.elemento()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 94
                self.match(BricolagemParser.VIRGULA)
                self.state = 95
                self.elemento()
                self.state = 100
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


        def getRuleIndex(self):
            return BricolagemParser.RULE_elemento

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PNivelContext(ElementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ElementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nivel(self):
            return self.getTypedRuleContext(BricolagemParser.NivelContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPNivel" ):
                listener.enterPNivel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPNivel" ):
                listener.exitPNivel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPNivel" ):
                return visitor.visitPNivel(self)
            else:
                return visitor.visitChildren(self)


    class PRecursosProjetoContext(ElementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ElementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def recursosProjeto(self):
            return self.getTypedRuleContext(BricolagemParser.RecursosProjetoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPRecursosProjeto" ):
                listener.enterPRecursosProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPRecursosProjeto" ):
                listener.exitPRecursosProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPRecursosProjeto" ):
                return visitor.visitPRecursosProjeto(self)
            else:
                return visitor.visitChildren(self)


    class PAtividadesProjetoContext(ElementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ElementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atividadesProjeto(self):
            return self.getTypedRuleContext(BricolagemParser.AtividadesProjetoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPAtividadesProjeto" ):
                listener.enterPAtividadesProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPAtividadesProjeto" ):
                listener.exitPAtividadesProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPAtividadesProjeto" ):
                return visitor.visitPAtividadesProjeto(self)
            else:
                return visitor.visitChildren(self)


    class PTemaContext(ElementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ElementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tema(self):
            return self.getTypedRuleContext(BricolagemParser.TemaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPTema" ):
                listener.enterPTema(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPTema" ):
                listener.exitPTema(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPTema" ):
                return visitor.visitPTema(self)
            else:
                return visitor.visitChildren(self)


    class PAvaliacaoProjetoContext(ElementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ElementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def avaliacaoProjeto(self):
            return self.getTypedRuleContext(BricolagemParser.AvaliacaoProjetoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPAvaliacaoProjeto" ):
                listener.enterPAvaliacaoProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPAvaliacaoProjeto" ):
                listener.exitPAvaliacaoProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPAvaliacaoProjeto" ):
                return visitor.visitPAvaliacaoProjeto(self)
            else:
                return visitor.visitChildren(self)


    class PConformidadeProjetoBNCCContext(ElementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ElementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conformidadeProjetoBNCC(self):
            return self.getTypedRuleContext(BricolagemParser.ConformidadeProjetoBNCCContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPConformidadeProjetoBNCC" ):
                listener.enterPConformidadeProjetoBNCC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPConformidadeProjetoBNCC" ):
                listener.exitPConformidadeProjetoBNCC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPConformidadeProjetoBNCC" ):
                return visitor.visitPConformidadeProjetoBNCC(self)
            else:
                return visitor.visitChildren(self)


    class PObjetivosProjetoContext(ElementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ElementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def objetivosProjeto(self):
            return self.getTypedRuleContext(BricolagemParser.ObjetivosProjetoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivosProjeto" ):
                listener.enterPObjetivosProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivosProjeto" ):
                listener.exitPObjetivosProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivosProjeto" ):
                return visitor.visitPObjetivosProjeto(self)
            else:
                return visitor.visitChildren(self)



    def elemento(self):

        localctx = BricolagemParser.ElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_elemento)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = BricolagemParser.PNivelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.nivel()
                pass
            elif token in [3]:
                localctx = BricolagemParser.PTemaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.tema()
                pass
            elif token in [4, 5, 6, 7]:
                localctx = BricolagemParser.PObjetivosProjetoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.objetivosProjeto()
                pass
            elif token in [8]:
                localctx = BricolagemParser.PAtividadesProjetoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.atividadesProjeto()
                pass
            elif token in [9]:
                localctx = BricolagemParser.PAvaliacaoProjetoContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 105
                self.avaliacaoProjeto()
                pass
            elif token in [10]:
                localctx = BricolagemParser.PRecursosProjetoContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 106
                self.recursosProjeto()
                pass
            elif token in [11]:
                localctx = BricolagemParser.PConformidadeProjetoBNCCContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 107
                self.conformidadeProjetoBNCC()
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


    class NivelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIVEL(self):
            return self.getToken(BricolagemParser.NIVEL, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_nivel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNivel" ):
                listener.enterNivel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNivel" ):
                listener.exitNivel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNivel" ):
                return visitor.visitNivel(self)
            else:
                return visitor.visitChildren(self)




    def nivel(self):

        localctx = BricolagemParser.NivelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nivel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BricolagemParser.NIVEL)
            self.state = 111
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 112
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMA(self):
            return self.getToken(BricolagemParser.TEMA, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_tema

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTema" ):
                listener.enterTema(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTema" ):
                listener.exitTema(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTema" ):
                return visitor.visitTema(self)
            else:
                return visitor.visitChildren(self)




    def tema(self):

        localctx = BricolagemParser.TemaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tema)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(BricolagemParser.TEMA)
            self.state = 115
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 116
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetivosProjetoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objetivo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.ObjetivoContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.ObjetivoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_objetivosProjeto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjetivosProjeto" ):
                listener.enterObjetivosProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjetivosProjeto" ):
                listener.exitObjetivosProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjetivosProjeto" ):
                return visitor.visitObjetivosProjeto(self)
            else:
                return visitor.visitChildren(self)




    def objetivosProjeto(self):

        localctx = BricolagemParser.ObjetivosProjetoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_objetivosProjeto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.objetivo()
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119
                    self.match(BricolagemParser.VIRGULA)
                    self.state = 120
                    self.objetivo() 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_objetivo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PObjetivosEducacionaisContext(ObjetivoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ObjetivoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJETIVO_EDUCACIONAL(self):
            return self.getToken(BricolagemParser.OBJETIVO_EDUCACIONAL, 0)
        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)
        def listaObjetivosEducacionais(self):
            return self.getTypedRuleContext(BricolagemParser.ListaObjetivosEducacionaisContext,0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivosEducacionais" ):
                listener.enterPObjetivosEducacionais(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivosEducacionais" ):
                listener.exitPObjetivosEducacionais(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivosEducacionais" ):
                return visitor.visitPObjetivosEducacionais(self)
            else:
                return visitor.visitChildren(self)


    class PObjetivosEnsinoContext(ObjetivoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ObjetivoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJETIVO_ENSINO(self):
            return self.getToken(BricolagemParser.OBJETIVO_ENSINO, 0)
        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)
        def listaObjetivosEnsino(self):
            return self.getTypedRuleContext(BricolagemParser.ListaObjetivosEnsinoContext,0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivosEnsino" ):
                listener.enterPObjetivosEnsino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivosEnsino" ):
                listener.exitPObjetivosEnsino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivosEnsino" ):
                return visitor.visitPObjetivosEnsino(self)
            else:
                return visitor.visitChildren(self)


    class PObjetivosPesquisaContext(ObjetivoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ObjetivoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJETIVO_PESQUISA(self):
            return self.getToken(BricolagemParser.OBJETIVO_PESQUISA, 0)
        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)
        def listaObjetivosPesquisa(self):
            return self.getTypedRuleContext(BricolagemParser.ListaObjetivosPesquisaContext,0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivosPesquisa" ):
                listener.enterPObjetivosPesquisa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivosPesquisa" ):
                listener.exitPObjetivosPesquisa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivosPesquisa" ):
                return visitor.visitPObjetivosPesquisa(self)
            else:
                return visitor.visitChildren(self)


    class PObjetivosAprendizagemContext(ObjetivoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ObjetivoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJETIVO_APRENDIZAGEM(self):
            return self.getToken(BricolagemParser.OBJETIVO_APRENDIZAGEM, 0)
        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)
        def listaObjetivosAprendizagem(self):
            return self.getTypedRuleContext(BricolagemParser.ListaObjetivosAprendizagemContext,0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivosAprendizagem" ):
                listener.enterPObjetivosAprendizagem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivosAprendizagem" ):
                listener.exitPObjetivosAprendizagem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivosAprendizagem" ):
                return visitor.visitPObjetivosAprendizagem(self)
            else:
                return visitor.visitChildren(self)



    def objetivo(self):

        localctx = BricolagemParser.ObjetivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_objetivo)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = BricolagemParser.PObjetivosEnsinoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(BricolagemParser.OBJETIVO_ENSINO)
                self.state = 127
                self.match(BricolagemParser.DOIS_PONTOS)
                self.state = 128
                self.match(BricolagemParser.ABRE_COLCHETE)
                self.state = 129
                self.listaObjetivosEnsino()
                self.state = 130
                self.match(BricolagemParser.FECHA_COLCHETE)
                pass
            elif token in [5]:
                localctx = BricolagemParser.PObjetivosAprendizagemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(BricolagemParser.OBJETIVO_APRENDIZAGEM)
                self.state = 133
                self.match(BricolagemParser.DOIS_PONTOS)
                self.state = 134
                self.match(BricolagemParser.ABRE_COLCHETE)
                self.state = 135
                self.listaObjetivosAprendizagem()
                self.state = 136
                self.match(BricolagemParser.FECHA_COLCHETE)
                pass
            elif token in [6]:
                localctx = BricolagemParser.PObjetivosPesquisaContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.match(BricolagemParser.OBJETIVO_PESQUISA)
                self.state = 139
                self.match(BricolagemParser.DOIS_PONTOS)
                self.state = 140
                self.match(BricolagemParser.ABRE_COLCHETE)
                self.state = 141
                self.listaObjetivosPesquisa()
                self.state = 142
                self.match(BricolagemParser.FECHA_COLCHETE)
                pass
            elif token in [7]:
                localctx = BricolagemParser.PObjetivosEducacionaisContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.match(BricolagemParser.OBJETIVO_EDUCACIONAL)
                self.state = 145
                self.match(BricolagemParser.DOIS_PONTOS)
                self.state = 146
                self.match(BricolagemParser.ABRE_COLCHETE)
                self.state = 147
                self.listaObjetivosEducacionais()
                self.state = 148
                self.match(BricolagemParser.FECHA_COLCHETE)
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


    class ListaObjetivosEnsinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objetivoEnsino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.ObjetivoEnsinoContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.ObjetivoEnsinoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_listaObjetivosEnsino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaObjetivosEnsino" ):
                listener.enterListaObjetivosEnsino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaObjetivosEnsino" ):
                listener.exitListaObjetivosEnsino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaObjetivosEnsino" ):
                return visitor.visitListaObjetivosEnsino(self)
            else:
                return visitor.visitChildren(self)




    def listaObjetivosEnsino(self):

        localctx = BricolagemParser.ListaObjetivosEnsinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listaObjetivosEnsino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 152
                self.objetivoEnsino()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 153
                    self.match(BricolagemParser.VIRGULA)
                    self.state = 154
                    self.objetivoEnsino()
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetivoEnsinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_objetivoEnsino

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PObjetivoEnsinoContext(ObjetivoEnsinoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ObjetivoEnsinoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def idObjetivoEnsino(self):
            return self.getTypedRuleContext(BricolagemParser.IdObjetivoEnsinoContext,0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def descricaoObjetivoEnsino(self):
            return self.getTypedRuleContext(BricolagemParser.DescricaoObjetivoEnsinoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivoEnsino" ):
                listener.enterPObjetivoEnsino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivoEnsino" ):
                listener.exitPObjetivoEnsino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivoEnsino" ):
                return visitor.visitPObjetivoEnsino(self)
            else:
                return visitor.visitChildren(self)



    def objetivoEnsino(self):

        localctx = BricolagemParser.ObjetivoEnsinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_objetivoEnsino)
        try:
            localctx = BricolagemParser.PObjetivoEnsinoContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.idObjetivoEnsino()
            self.state = 163
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 164
            self.descricaoObjetivoEnsino()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdObjetivoEnsinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BricolagemParser.ID, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_idObjetivoEnsino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdObjetivoEnsino" ):
                listener.enterIdObjetivoEnsino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdObjetivoEnsino" ):
                listener.exitIdObjetivoEnsino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdObjetivoEnsino" ):
                return visitor.visitIdObjetivoEnsino(self)
            else:
                return visitor.visitChildren(self)




    def idObjetivoEnsino(self):

        localctx = BricolagemParser.IdObjetivoEnsinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idObjetivoEnsino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BricolagemParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescricaoObjetivoEnsinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_descricaoObjetivoEnsino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescricaoObjetivoEnsino" ):
                listener.enterDescricaoObjetivoEnsino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescricaoObjetivoEnsino" ):
                listener.exitDescricaoObjetivoEnsino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescricaoObjetivoEnsino" ):
                return visitor.visitDescricaoObjetivoEnsino(self)
            else:
                return visitor.visitChildren(self)




    def descricaoObjetivoEnsino(self):

        localctx = BricolagemParser.DescricaoObjetivoEnsinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_descricaoObjetivoEnsino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaObjetivosAprendizagemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objetivoAprendizagem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.ObjetivoAprendizagemContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.ObjetivoAprendizagemContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_listaObjetivosAprendizagem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaObjetivosAprendizagem" ):
                listener.enterListaObjetivosAprendizagem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaObjetivosAprendizagem" ):
                listener.exitListaObjetivosAprendizagem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaObjetivosAprendizagem" ):
                return visitor.visitListaObjetivosAprendizagem(self)
            else:
                return visitor.visitChildren(self)




    def listaObjetivosAprendizagem(self):

        localctx = BricolagemParser.ListaObjetivosAprendizagemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listaObjetivosAprendizagem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 170
                self.objetivoAprendizagem()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 171
                    self.match(BricolagemParser.VIRGULA)
                    self.state = 172
                    self.objetivoAprendizagem()
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetivoAprendizagemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_objetivoAprendizagem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PObjetivoAprendizagenContext(ObjetivoAprendizagemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ObjetivoAprendizagemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def idObjetivoAprendizagem(self):
            return self.getTypedRuleContext(BricolagemParser.IdObjetivoAprendizagemContext,0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def descricaoObjetivoAprendizagem(self):
            return self.getTypedRuleContext(BricolagemParser.DescricaoObjetivoAprendizagemContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivoAprendizagen" ):
                listener.enterPObjetivoAprendizagen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivoAprendizagen" ):
                listener.exitPObjetivoAprendizagen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivoAprendizagen" ):
                return visitor.visitPObjetivoAprendizagen(self)
            else:
                return visitor.visitChildren(self)



    def objetivoAprendizagem(self):

        localctx = BricolagemParser.ObjetivoAprendizagemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_objetivoAprendizagem)
        try:
            localctx = BricolagemParser.PObjetivoAprendizagenContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.idObjetivoAprendizagem()
            self.state = 181
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 182
            self.descricaoObjetivoAprendizagem()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdObjetivoAprendizagemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BricolagemParser.ID, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_idObjetivoAprendizagem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdObjetivoAprendizagem" ):
                listener.enterIdObjetivoAprendizagem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdObjetivoAprendizagem" ):
                listener.exitIdObjetivoAprendizagem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdObjetivoAprendizagem" ):
                return visitor.visitIdObjetivoAprendizagem(self)
            else:
                return visitor.visitChildren(self)




    def idObjetivoAprendizagem(self):

        localctx = BricolagemParser.IdObjetivoAprendizagemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_idObjetivoAprendizagem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BricolagemParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescricaoObjetivoAprendizagemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_descricaoObjetivoAprendizagem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescricaoObjetivoAprendizagem" ):
                listener.enterDescricaoObjetivoAprendizagem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescricaoObjetivoAprendizagem" ):
                listener.exitDescricaoObjetivoAprendizagem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescricaoObjetivoAprendizagem" ):
                return visitor.visitDescricaoObjetivoAprendizagem(self)
            else:
                return visitor.visitChildren(self)




    def descricaoObjetivoAprendizagem(self):

        localctx = BricolagemParser.DescricaoObjetivoAprendizagemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_descricaoObjetivoAprendizagem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaObjetivosPesquisaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objetivoPesquisa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.ObjetivoPesquisaContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.ObjetivoPesquisaContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_listaObjetivosPesquisa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaObjetivosPesquisa" ):
                listener.enterListaObjetivosPesquisa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaObjetivosPesquisa" ):
                listener.exitListaObjetivosPesquisa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaObjetivosPesquisa" ):
                return visitor.visitListaObjetivosPesquisa(self)
            else:
                return visitor.visitChildren(self)




    def listaObjetivosPesquisa(self):

        localctx = BricolagemParser.ListaObjetivosPesquisaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listaObjetivosPesquisa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 188
                self.objetivoPesquisa()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 189
                    self.match(BricolagemParser.VIRGULA)
                    self.state = 190
                    self.objetivoPesquisa()
                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetivoPesquisaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_objetivoPesquisa

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PObjetivoPesquisaContext(ObjetivoPesquisaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ObjetivoPesquisaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def idObjetivoPesquisa(self):
            return self.getTypedRuleContext(BricolagemParser.IdObjetivoPesquisaContext,0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def descricaoObjetivoPesquisa(self):
            return self.getTypedRuleContext(BricolagemParser.DescricaoObjetivoPesquisaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivoPesquisa" ):
                listener.enterPObjetivoPesquisa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivoPesquisa" ):
                listener.exitPObjetivoPesquisa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivoPesquisa" ):
                return visitor.visitPObjetivoPesquisa(self)
            else:
                return visitor.visitChildren(self)



    def objetivoPesquisa(self):

        localctx = BricolagemParser.ObjetivoPesquisaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_objetivoPesquisa)
        try:
            localctx = BricolagemParser.PObjetivoPesquisaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.idObjetivoPesquisa()
            self.state = 199
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 200
            self.descricaoObjetivoPesquisa()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdObjetivoPesquisaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BricolagemParser.ID, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_idObjetivoPesquisa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdObjetivoPesquisa" ):
                listener.enterIdObjetivoPesquisa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdObjetivoPesquisa" ):
                listener.exitIdObjetivoPesquisa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdObjetivoPesquisa" ):
                return visitor.visitIdObjetivoPesquisa(self)
            else:
                return visitor.visitChildren(self)




    def idObjetivoPesquisa(self):

        localctx = BricolagemParser.IdObjetivoPesquisaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_idObjetivoPesquisa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(BricolagemParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescricaoObjetivoPesquisaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_descricaoObjetivoPesquisa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescricaoObjetivoPesquisa" ):
                listener.enterDescricaoObjetivoPesquisa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescricaoObjetivoPesquisa" ):
                listener.exitDescricaoObjetivoPesquisa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescricaoObjetivoPesquisa" ):
                return visitor.visitDescricaoObjetivoPesquisa(self)
            else:
                return visitor.visitChildren(self)




    def descricaoObjetivoPesquisa(self):

        localctx = BricolagemParser.DescricaoObjetivoPesquisaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_descricaoObjetivoPesquisa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaObjetivosEducacionaisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objetivoEducacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.ObjetivoEducacionalContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.ObjetivoEducacionalContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_listaObjetivosEducacionais

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaObjetivosEducacionais" ):
                listener.enterListaObjetivosEducacionais(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaObjetivosEducacionais" ):
                listener.exitListaObjetivosEducacionais(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaObjetivosEducacionais" ):
                return visitor.visitListaObjetivosEducacionais(self)
            else:
                return visitor.visitChildren(self)




    def listaObjetivosEducacionais(self):

        localctx = BricolagemParser.ListaObjetivosEducacionaisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_listaObjetivosEducacionais)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 206
                self.objetivoEducacional()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 207
                    self.match(BricolagemParser.VIRGULA)
                    self.state = 208
                    self.objetivoEducacional()
                    self.state = 213
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetivoEducacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_objetivoEducacional

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PObjetivoEducacionalContext(ObjetivoEducacionalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.ObjetivoEducacionalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def idObjetivoEducacional(self):
            return self.getTypedRuleContext(BricolagemParser.IdObjetivoEducacionalContext,0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def descricaoObjetivoEducacional(self):
            return self.getTypedRuleContext(BricolagemParser.DescricaoObjetivoEducacionalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPObjetivoEducacional" ):
                listener.enterPObjetivoEducacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPObjetivoEducacional" ):
                listener.exitPObjetivoEducacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPObjetivoEducacional" ):
                return visitor.visitPObjetivoEducacional(self)
            else:
                return visitor.visitChildren(self)



    def objetivoEducacional(self):

        localctx = BricolagemParser.ObjetivoEducacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_objetivoEducacional)
        try:
            localctx = BricolagemParser.PObjetivoEducacionalContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.idObjetivoEducacional()
            self.state = 217
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 218
            self.descricaoObjetivoEducacional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdObjetivoEducacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BricolagemParser.ID, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_idObjetivoEducacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdObjetivoEducacional" ):
                listener.enterIdObjetivoEducacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdObjetivoEducacional" ):
                listener.exitIdObjetivoEducacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdObjetivoEducacional" ):
                return visitor.visitIdObjetivoEducacional(self)
            else:
                return visitor.visitChildren(self)




    def idObjetivoEducacional(self):

        localctx = BricolagemParser.IdObjetivoEducacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_idObjetivoEducacional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BricolagemParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescricaoObjetivoEducacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_descricaoObjetivoEducacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescricaoObjetivoEducacional" ):
                listener.enterDescricaoObjetivoEducacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescricaoObjetivoEducacional" ):
                listener.exitDescricaoObjetivoEducacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescricaoObjetivoEducacional" ):
                return visitor.visitDescricaoObjetivoEducacional(self)
            else:
                return visitor.visitChildren(self)




    def descricaoObjetivoEducacional(self):

        localctx = BricolagemParser.DescricaoObjetivoEducacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_descricaoObjetivoEducacional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtividadesProjetoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATIVIDADES(self):
            return self.getToken(BricolagemParser.ATIVIDADES, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)

        def listaAtividades(self):
            return self.getTypedRuleContext(BricolagemParser.ListaAtividadesContext,0)


        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_atividadesProjeto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtividadesProjeto" ):
                listener.enterAtividadesProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtividadesProjeto" ):
                listener.exitAtividadesProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtividadesProjeto" ):
                return visitor.visitAtividadesProjeto(self)
            else:
                return visitor.visitChildren(self)




    def atividadesProjeto(self):

        localctx = BricolagemParser.AtividadesProjetoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_atividadesProjeto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(BricolagemParser.ATIVIDADES)
            self.state = 225
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 226
            self.match(BricolagemParser.ABRE_COLCHETE)
            self.state = 227
            self.listaAtividades()
            self.state = 228
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaAtividadesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atividade(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.AtividadeContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.AtividadeContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_listaAtividades

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaAtividades" ):
                listener.enterListaAtividades(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaAtividades" ):
                listener.exitListaAtividades(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAtividades" ):
                return visitor.visitListaAtividades(self)
            else:
                return visitor.visitChildren(self)




    def listaAtividades(self):

        localctx = BricolagemParser.ListaAtividadesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_listaAtividades)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 230
                self.atividade()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 231
                    self.match(BricolagemParser.VIRGULA)
                    self.state = 232
                    self.atividade()
                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtividadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_atividade

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PAtividadeContext(AtividadeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.AtividadeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nomeAtividade(self):
            return self.getTypedRuleContext(BricolagemParser.NomeAtividadeContext,0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)
        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)
        def listaComponentesAtividade(self):
            return self.getTypedRuleContext(BricolagemParser.ListaComponentesAtividadeContext,0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPAtividade" ):
                listener.enterPAtividade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPAtividade" ):
                listener.exitPAtividade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPAtividade" ):
                return visitor.visitPAtividade(self)
            else:
                return visitor.visitChildren(self)



    def atividade(self):

        localctx = BricolagemParser.AtividadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_atividade)
        try:
            localctx = BricolagemParser.PAtividadeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.nomeAtividade()
            self.state = 241
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 242
            self.match(BricolagemParser.ABRE_COLCHETE)
            self.state = 243
            self.listaComponentesAtividade()
            self.state = 244
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NomeAtividadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_nomeAtividade

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PNomeAtividadeContext(NomeAtividadeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.NomeAtividadeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPNomeAtividade" ):
                listener.enterPNomeAtividade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPNomeAtividade" ):
                listener.exitPNomeAtividade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPNomeAtividade" ):
                return visitor.visitPNomeAtividade(self)
            else:
                return visitor.visitChildren(self)



    def nomeAtividade(self):

        localctx = BricolagemParser.NomeAtividadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_nomeAtividade)
        try:
            localctx = BricolagemParser.PNomeAtividadeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaComponentesAtividadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def componenteAtividade(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.ComponenteAtividadeContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.ComponenteAtividadeContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_listaComponentesAtividade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaComponentesAtividade" ):
                listener.enterListaComponentesAtividade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaComponentesAtividade" ):
                listener.exitListaComponentesAtividade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaComponentesAtividade" ):
                return visitor.visitListaComponentesAtividade(self)
            else:
                return visitor.visitChildren(self)




    def listaComponentesAtividade(self):

        localctx = BricolagemParser.ListaComponentesAtividadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_listaComponentesAtividade)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0):
                self.state = 248
                self.componenteAtividade()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 249
                    self.match(BricolagemParser.VIRGULA)
                    self.state = 250
                    self.componenteAtividade()
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponenteAtividadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def descricaoAtividade(self):
            return self.getTypedRuleContext(BricolagemParser.DescricaoAtividadeContext,0)


        def duracaoAtividade(self):
            return self.getTypedRuleContext(BricolagemParser.DuracaoAtividadeContext,0)


        def passosAtividade(self):
            return self.getTypedRuleContext(BricolagemParser.PassosAtividadeContext,0)


        def getRuleIndex(self):
            return BricolagemParser.RULE_componenteAtividade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponenteAtividade" ):
                listener.enterComponenteAtividade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponenteAtividade" ):
                listener.exitComponenteAtividade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponenteAtividade" ):
                return visitor.visitComponenteAtividade(self)
            else:
                return visitor.visitChildren(self)




    def componenteAtividade(self):

        localctx = BricolagemParser.ComponenteAtividadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_componenteAtividade)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.descricaoAtividade()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.duracaoAtividade()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.passosAtividade()
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


    class DescricaoAtividadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCRICAO(self):
            return self.getToken(BricolagemParser.DESCRICAO, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_descricaoAtividade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescricaoAtividade" ):
                listener.enterDescricaoAtividade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescricaoAtividade" ):
                listener.exitDescricaoAtividade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescricaoAtividade" ):
                return visitor.visitDescricaoAtividade(self)
            else:
                return visitor.visitChildren(self)




    def descricaoAtividade(self):

        localctx = BricolagemParser.DescricaoAtividadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_descricaoAtividade)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(BricolagemParser.DESCRICAO)
            self.state = 264
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 265
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DuracaoAtividadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DURACAOMINUTOS(self):
            return self.getToken(BricolagemParser.DURACAOMINUTOS, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def NUMERO(self):
            return self.getToken(BricolagemParser.NUMERO, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_duracaoAtividade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDuracaoAtividade" ):
                listener.enterDuracaoAtividade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDuracaoAtividade" ):
                listener.exitDuracaoAtividade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDuracaoAtividade" ):
                return visitor.visitDuracaoAtividade(self)
            else:
                return visitor.visitChildren(self)




    def duracaoAtividade(self):

        localctx = BricolagemParser.DuracaoAtividadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_duracaoAtividade)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BricolagemParser.DURACAOMINUTOS)
            self.state = 268
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 269
            self.match(BricolagemParser.NUMERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassosAtividadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASSOS(self):
            return self.getToken(BricolagemParser.PASSOS, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def passoAtividade(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.PassoAtividadeContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.PassoAtividadeContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_passosAtividade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassosAtividade" ):
                listener.enterPassosAtividade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassosAtividade" ):
                listener.exitPassosAtividade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassosAtividade" ):
                return visitor.visitPassosAtividade(self)
            else:
                return visitor.visitChildren(self)




    def passosAtividade(self):

        localctx = BricolagemParser.PassosAtividadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_passosAtividade)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(BricolagemParser.PASSOS)
            self.state = 272
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 273
            self.match(BricolagemParser.ABRE_COLCHETE)

            self.state = 274
            self.passoAtividade()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 275
                self.match(BricolagemParser.VIRGULA)
                self.state = 276
                self.passoAtividade()
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassoAtividadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_passoAtividade

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PPassoAtividadeContext(PassoAtividadeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.PassoAtividadeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPPassoAtividade" ):
                listener.enterPPassoAtividade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPPassoAtividade" ):
                listener.exitPPassoAtividade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPPassoAtividade" ):
                return visitor.visitPPassoAtividade(self)
            else:
                return visitor.visitChildren(self)



    def passoAtividade(self):

        localctx = BricolagemParser.PassoAtividadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_passoAtividade)
        try:
            localctx = BricolagemParser.PPassoAtividadeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AvaliacaoProjetoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AVALIACAO(self):
            return self.getToken(BricolagemParser.AVALIACAO, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)

        def listaComponentesAvaliacao(self):
            return self.getTypedRuleContext(BricolagemParser.ListaComponentesAvaliacaoContext,0)


        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def getRuleIndex(self):
            return BricolagemParser.RULE_avaliacaoProjeto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvaliacaoProjeto" ):
                listener.enterAvaliacaoProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvaliacaoProjeto" ):
                listener.exitAvaliacaoProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAvaliacaoProjeto" ):
                return visitor.visitAvaliacaoProjeto(self)
            else:
                return visitor.visitChildren(self)




    def avaliacaoProjeto(self):

        localctx = BricolagemParser.AvaliacaoProjetoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_avaliacaoProjeto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(BricolagemParser.AVALIACAO)
            self.state = 287
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 288
            self.match(BricolagemParser.ABRE_COLCHETE)
            self.state = 289
            self.listaComponentesAvaliacao()
            self.state = 290
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaComponentesAvaliacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def componenteAvaliacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.ComponenteAvaliacaoContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.ComponenteAvaliacaoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_listaComponentesAvaliacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaComponentesAvaliacao" ):
                listener.enterListaComponentesAvaliacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaComponentesAvaliacao" ):
                listener.exitListaComponentesAvaliacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaComponentesAvaliacao" ):
                return visitor.visitListaComponentesAvaliacao(self)
            else:
                return visitor.visitChildren(self)




    def listaComponentesAvaliacao(self):

        localctx = BricolagemParser.ListaComponentesAvaliacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_listaComponentesAvaliacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15 or _la==16:
                self.state = 292
                self.componenteAvaliacao()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 293
                    self.match(BricolagemParser.VIRGULA)
                    self.state = 294
                    self.componenteAvaliacao()
                    self.state = 299
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponenteAvaliacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def criteriosAvaliacao(self):
            return self.getTypedRuleContext(BricolagemParser.CriteriosAvaliacaoContext,0)


        def instrumentosAvaliacao(self):
            return self.getTypedRuleContext(BricolagemParser.InstrumentosAvaliacaoContext,0)


        def getRuleIndex(self):
            return BricolagemParser.RULE_componenteAvaliacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponenteAvaliacao" ):
                listener.enterComponenteAvaliacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponenteAvaliacao" ):
                listener.exitComponenteAvaliacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponenteAvaliacao" ):
                return visitor.visitComponenteAvaliacao(self)
            else:
                return visitor.visitChildren(self)




    def componenteAvaliacao(self):

        localctx = BricolagemParser.ComponenteAvaliacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_componenteAvaliacao)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.criteriosAvaliacao()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.instrumentosAvaliacao()
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


    class CriteriosAvaliacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CRITERIOS(self):
            return self.getToken(BricolagemParser.CRITERIOS, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def criterioAvaliacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.CriterioAvaliacaoContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.CriterioAvaliacaoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_criteriosAvaliacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCriteriosAvaliacao" ):
                listener.enterCriteriosAvaliacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCriteriosAvaliacao" ):
                listener.exitCriteriosAvaliacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCriteriosAvaliacao" ):
                return visitor.visitCriteriosAvaliacao(self)
            else:
                return visitor.visitChildren(self)




    def criteriosAvaliacao(self):

        localctx = BricolagemParser.CriteriosAvaliacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_criteriosAvaliacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(BricolagemParser.CRITERIOS)
            self.state = 307
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 308
            self.match(BricolagemParser.ABRE_COLCHETE)

            self.state = 309
            self.criterioAvaliacao()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 310
                self.match(BricolagemParser.VIRGULA)
                self.state = 311
                self.criterioAvaliacao()
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 317
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CriterioAvaliacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_criterioAvaliacao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PCriterioAvaliacaoContext(CriterioAvaliacaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.CriterioAvaliacaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPCriterioAvaliacao" ):
                listener.enterPCriterioAvaliacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPCriterioAvaliacao" ):
                listener.exitPCriterioAvaliacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPCriterioAvaliacao" ):
                return visitor.visitPCriterioAvaliacao(self)
            else:
                return visitor.visitChildren(self)



    def criterioAvaliacao(self):

        localctx = BricolagemParser.CriterioAvaliacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_criterioAvaliacao)
        try:
            localctx = BricolagemParser.PCriterioAvaliacaoContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrumentosAvaliacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTRUMENTOS(self):
            return self.getToken(BricolagemParser.INSTRUMENTOS, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def instrumentoAvaliacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.InstrumentoAvaliacaoContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.InstrumentoAvaliacaoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_instrumentosAvaliacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrumentosAvaliacao" ):
                listener.enterInstrumentosAvaliacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrumentosAvaliacao" ):
                listener.exitInstrumentosAvaliacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrumentosAvaliacao" ):
                return visitor.visitInstrumentosAvaliacao(self)
            else:
                return visitor.visitChildren(self)




    def instrumentosAvaliacao(self):

        localctx = BricolagemParser.InstrumentosAvaliacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_instrumentosAvaliacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(BricolagemParser.INSTRUMENTOS)
            self.state = 322
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 323
            self.match(BricolagemParser.ABRE_COLCHETE)

            self.state = 324
            self.instrumentoAvaliacao()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 325
                self.match(BricolagemParser.VIRGULA)
                self.state = 326
                self.instrumentoAvaliacao()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 332
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrumentoAvaliacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_instrumentoAvaliacao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PInstrumentoAvaliacaoContext(InstrumentoAvaliacaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.InstrumentoAvaliacaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPInstrumentoAvaliacao" ):
                listener.enterPInstrumentoAvaliacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPInstrumentoAvaliacao" ):
                listener.exitPInstrumentoAvaliacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPInstrumentoAvaliacao" ):
                return visitor.visitPInstrumentoAvaliacao(self)
            else:
                return visitor.visitChildren(self)



    def instrumentoAvaliacao(self):

        localctx = BricolagemParser.InstrumentoAvaliacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_instrumentoAvaliacao)
        try:
            localctx = BricolagemParser.PInstrumentoAvaliacaoContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecursosProjetoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECURSOS(self):
            return self.getToken(BricolagemParser.RECURSOS, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def recurso(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.RecursoContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.RecursoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_recursosProjeto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecursosProjeto" ):
                listener.enterRecursosProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecursosProjeto" ):
                listener.exitRecursosProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecursosProjeto" ):
                return visitor.visitRecursosProjeto(self)
            else:
                return visitor.visitChildren(self)




    def recursosProjeto(self):

        localctx = BricolagemParser.RecursosProjetoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_recursosProjeto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(BricolagemParser.RECURSOS)
            self.state = 337
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 338
            self.match(BricolagemParser.ABRE_COLCHETE)

            self.state = 339
            self.recurso()
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 340
                self.match(BricolagemParser.VIRGULA)
                self.state = 341
                self.recurso()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 347
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecursoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_recurso

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PRecursoProjetoContext(RecursoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.RecursoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BricolagemParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPRecursoProjeto" ):
                listener.enterPRecursoProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPRecursoProjeto" ):
                listener.exitPRecursoProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPRecursoProjeto" ):
                return visitor.visitPRecursoProjeto(self)
            else:
                return visitor.visitChildren(self)



    def recurso(self):

        localctx = BricolagemParser.RecursoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_recurso)
        try:
            localctx = BricolagemParser.PRecursoProjetoContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(BricolagemParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConformidadeProjetoBNCCContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONFORMIDADE_BNCC(self):
            return self.getToken(BricolagemParser.CONFORMIDADE_BNCC, 0)

        def DOIS_PONTOS(self):
            return self.getToken(BricolagemParser.DOIS_PONTOS, 0)

        def ABRE_COLCHETE(self):
            return self.getToken(BricolagemParser.ABRE_COLCHETE, 0)

        def FECHA_COLCHETE(self):
            return self.getToken(BricolagemParser.FECHA_COLCHETE, 0)

        def idBNCC(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BricolagemParser.IdBNCCContext)
            else:
                return self.getTypedRuleContext(BricolagemParser.IdBNCCContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(BricolagemParser.VIRGULA)
            else:
                return self.getToken(BricolagemParser.VIRGULA, i)

        def getRuleIndex(self):
            return BricolagemParser.RULE_conformidadeProjetoBNCC

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConformidadeProjetoBNCC" ):
                listener.enterConformidadeProjetoBNCC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConformidadeProjetoBNCC" ):
                listener.exitConformidadeProjetoBNCC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConformidadeProjetoBNCC" ):
                return visitor.visitConformidadeProjetoBNCC(self)
            else:
                return visitor.visitChildren(self)




    def conformidadeProjetoBNCC(self):

        localctx = BricolagemParser.ConformidadeProjetoBNCCContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_conformidadeProjetoBNCC)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(BricolagemParser.CONFORMIDADE_BNCC)
            self.state = 352
            self.match(BricolagemParser.DOIS_PONTOS)
            self.state = 353
            self.match(BricolagemParser.ABRE_COLCHETE)

            self.state = 354
            self.idBNCC()
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 355
                self.match(BricolagemParser.VIRGULA)
                self.state = 356
                self.idBNCC()
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 362
            self.match(BricolagemParser.FECHA_COLCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdBNCCContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BricolagemParser.RULE_idBNCC

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PIDBNCCProjetoContext(IdBNCCContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BricolagemParser.IdBNCCContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BricolagemParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPIDBNCCProjeto" ):
                listener.enterPIDBNCCProjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPIDBNCCProjeto" ):
                listener.exitPIDBNCCProjeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPIDBNCCProjeto" ):
                return visitor.visitPIDBNCCProjeto(self)
            else:
                return visitor.visitChildren(self)



    def idBNCC(self):

        localctx = BricolagemParser.IdBNCCContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_idBNCC)
        try:
            localctx = BricolagemParser.PIDBNCCProjetoContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(BricolagemParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





