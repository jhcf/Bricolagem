// REGRAS SINTÁTICAS (PARSER)

parser grammar BricolagemParser;


options { tokenVocab=BricolagemLexer; }


projetoMaker: PROJETO_MAKER ABRE_COLCHETE listaElementos FECHA_COLCHETE;

listaElementos: elemento (VIRGULA elemento)*
;

elemento:
    nivel 				# PNivel
    | tema				# PTema
    | objetivosProjeto 			# PObjetivosProjeto
    | atividadesProjeto 		# PAtividadesProjeto
    | avaliacaoProjeto 			# PAvaliacaoProjeto
    | recursosProjeto 			# PRecursosProjeto
    | conformidadeProjetoBNCC		# PConformidadeProjetoBNCC
    ;	

nivel: NIVEL DOIS_PONTOS STRING
;

tema: TEMA DOIS_PONTOS STRING
;

objetivosProjeto: objetivo (VIRGULA objetivo)*
;

objetivo: 
    OBJETIVO_ENSINO DOIS_PONTOS ABRE_COLCHETE listaObjetivosEnsino FECHA_COLCHETE # PObjetivosEnsino
    | OBJETIVO_APRENDIZAGEM DOIS_PONTOS ABRE_COLCHETE listaObjetivosAprendizagem FECHA_COLCHETE  # PObjetivosAprendizagem
    | OBJETIVO_PESQUISA DOIS_PONTOS ABRE_COLCHETE listaObjetivosPesquisa FECHA_COLCHETE # PObjetivosPesquisa 
    | OBJETIVO_EDUCACIONAL DOIS_PONTOS ABRE_COLCHETE listaObjetivosEducacionais FECHA_COLCHETE # PObjetivosEducacionais
    ;

listaObjetivosEnsino: (objetivoEnsino (VIRGULA objetivoEnsino)*)?
;

objetivoEnsino: idObjetivoEnsino DOIS_PONTOS descricaoObjetivoEnsino # PObjetivoEnsino
;

idObjetivoEnsino: ID
;

descricaoObjetivoEnsino: STRING
;

listaObjetivosAprendizagem: (objetivoAprendizagem (VIRGULA objetivoAprendizagem)*)?
;

objetivoAprendizagem: idObjetivoAprendizagem DOIS_PONTOS descricaoObjetivoAprendizagem #PObjetivoAprendizagen
;

idObjetivoAprendizagem: ID
;
descricaoObjetivoAprendizagem: STRING
;


listaObjetivosPesquisa: (objetivoPesquisa (VIRGULA objetivoPesquisa)*)?
;

objetivoPesquisa: idObjetivoPesquisa DOIS_PONTOS descricaoObjetivoPesquisa  #PObjetivoPesquisa
;

idObjetivoPesquisa: ID
;
descricaoObjetivoPesquisa: STRING
;

listaObjetivosEducacionais: (objetivoEducacional (VIRGULA objetivoEducacional)*)?
;

objetivoEducacional: idObjetivoEducacional DOIS_PONTOS descricaoObjetivoEducacional # PObjetivoEducacional
;

idObjetivoEducacional: ID
;

descricaoObjetivoEducacional: STRING
;

atividadesProjeto: ATIVIDADES DOIS_PONTOS ABRE_COLCHETE listaAtividades FECHA_COLCHETE
;

listaAtividades: (atividade (VIRGULA atividade)*)?
;

atividade: nomeAtividade DOIS_PONTOS ABRE_COLCHETE listaComponentesAtividade FECHA_COLCHETE #PAtividade
;

nomeAtividade: STRING #PNomeAtividade
;

listaComponentesAtividade: (componenteAtividade (VIRGULA componenteAtividade)*)?
;

componenteAtividade:
	descricaoAtividade
	| duracaoAtividade
	| passosAtividade
	;

descricaoAtividade: DESCRICAO DOIS_PONTOS STRING
;

duracaoAtividade: DURACAOMINUTOS DOIS_PONTOS NUMERO
;
 
passosAtividade: PASSOS DOIS_PONTOS ABRE_COLCHETE (passoAtividade (VIRGULA passoAtividade)*) FECHA_COLCHETE
;

passoAtividade: STRING #PPassoAtividade
;

avaliacaoProjeto: AVALIACAO DOIS_PONTOS ABRE_COLCHETE listaComponentesAvaliacao FECHA_COLCHETE
;

listaComponentesAvaliacao: (componenteAvaliacao (VIRGULA componenteAvaliacao)*)?
;

componenteAvaliacao:
	criteriosAvaliacao
	| instrumentosAvaliacao
	;

criteriosAvaliacao: CRITERIOS DOIS_PONTOS ABRE_COLCHETE (criterioAvaliacao (VIRGULA criterioAvaliacao)*) FECHA_COLCHETE 
;
criterioAvaliacao: STRING 	# PCriterioAvaliacao
;

instrumentosAvaliacao: INSTRUMENTOS DOIS_PONTOS ABRE_COLCHETE (instrumentoAvaliacao (VIRGULA instrumentoAvaliacao)*) FECHA_COLCHETE
;
instrumentoAvaliacao: STRING	#PInstrumentoAvaliacao
;

recursosProjeto: RECURSOS DOIS_PONTOS ABRE_COLCHETE (recurso (VIRGULA recurso)*) FECHA_COLCHETE
;

recurso: STRING #PRecursoProjeto
;

conformidadeProjetoBNCC: CONFORMIDADE_BNCC DOIS_PONTOS ABRE_COLCHETE (idBNCC (VIRGULA idBNCC)*) FECHA_COLCHETE
;

idBNCC: ID #PIDBNCCProjeto
;
