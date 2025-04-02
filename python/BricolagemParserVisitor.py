# Generated from BricolagemParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BricolagemParser import BricolagemParser
else:
    from BricolagemParser import BricolagemParser

# This class defines a complete generic visitor for a parse tree produced by BricolagemParser.

class BricolagemParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BricolagemParser#projetoMaker.
    def visitProjetoMaker(self, ctx:BricolagemParser.ProjetoMakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#listaElementos.
    def visitListaElementos(self, ctx:BricolagemParser.ListaElementosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PNivel.
    def visitPNivel(self, ctx:BricolagemParser.PNivelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PTema.
    def visitPTema(self, ctx:BricolagemParser.PTemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivosProjeto.
    def visitPObjetivosProjeto(self, ctx:BricolagemParser.PObjetivosProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PAtividadesProjeto.
    def visitPAtividadesProjeto(self, ctx:BricolagemParser.PAtividadesProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PAvaliacaoProjeto.
    def visitPAvaliacaoProjeto(self, ctx:BricolagemParser.PAvaliacaoProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PRecursosProjeto.
    def visitPRecursosProjeto(self, ctx:BricolagemParser.PRecursosProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PConformidadeProjetoBNCC.
    def visitPConformidadeProjetoBNCC(self, ctx:BricolagemParser.PConformidadeProjetoBNCCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#nivel.
    def visitNivel(self, ctx:BricolagemParser.NivelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#tema.
    def visitTema(self, ctx:BricolagemParser.TemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#objetivosProjeto.
    def visitObjetivosProjeto(self, ctx:BricolagemParser.ObjetivosProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivosEnsino.
    def visitPObjetivosEnsino(self, ctx:BricolagemParser.PObjetivosEnsinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivosAprendizagem.
    def visitPObjetivosAprendizagem(self, ctx:BricolagemParser.PObjetivosAprendizagemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivosPesquisa.
    def visitPObjetivosPesquisa(self, ctx:BricolagemParser.PObjetivosPesquisaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivosEducacionais.
    def visitPObjetivosEducacionais(self, ctx:BricolagemParser.PObjetivosEducacionaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#listaObjetivosEnsino.
    def visitListaObjetivosEnsino(self, ctx:BricolagemParser.ListaObjetivosEnsinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivoEnsino.
    def visitPObjetivoEnsino(self, ctx:BricolagemParser.PObjetivoEnsinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#idObjetivoEnsino.
    def visitIdObjetivoEnsino(self, ctx:BricolagemParser.IdObjetivoEnsinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#descricaoObjetivoEnsino.
    def visitDescricaoObjetivoEnsino(self, ctx:BricolagemParser.DescricaoObjetivoEnsinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#listaObjetivosAprendizagem.
    def visitListaObjetivosAprendizagem(self, ctx:BricolagemParser.ListaObjetivosAprendizagemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivoAprendizagen.
    def visitPObjetivoAprendizagen(self, ctx:BricolagemParser.PObjetivoAprendizagenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#idObjetivoAprendizagem.
    def visitIdObjetivoAprendizagem(self, ctx:BricolagemParser.IdObjetivoAprendizagemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#descricaoObjetivoAprendizagem.
    def visitDescricaoObjetivoAprendizagem(self, ctx:BricolagemParser.DescricaoObjetivoAprendizagemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#listaObjetivosPesquisa.
    def visitListaObjetivosPesquisa(self, ctx:BricolagemParser.ListaObjetivosPesquisaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivoPesquisa.
    def visitPObjetivoPesquisa(self, ctx:BricolagemParser.PObjetivoPesquisaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#idObjetivoPesquisa.
    def visitIdObjetivoPesquisa(self, ctx:BricolagemParser.IdObjetivoPesquisaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#descricaoObjetivoPesquisa.
    def visitDescricaoObjetivoPesquisa(self, ctx:BricolagemParser.DescricaoObjetivoPesquisaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#listaObjetivosEducacionais.
    def visitListaObjetivosEducacionais(self, ctx:BricolagemParser.ListaObjetivosEducacionaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PObjetivoEducacional.
    def visitPObjetivoEducacional(self, ctx:BricolagemParser.PObjetivoEducacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#idObjetivoEducacional.
    def visitIdObjetivoEducacional(self, ctx:BricolagemParser.IdObjetivoEducacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#descricaoObjetivoEducacional.
    def visitDescricaoObjetivoEducacional(self, ctx:BricolagemParser.DescricaoObjetivoEducacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#atividadesProjeto.
    def visitAtividadesProjeto(self, ctx:BricolagemParser.AtividadesProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#listaAtividades.
    def visitListaAtividades(self, ctx:BricolagemParser.ListaAtividadesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PAtividade.
    def visitPAtividade(self, ctx:BricolagemParser.PAtividadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PNomeAtividade.
    def visitPNomeAtividade(self, ctx:BricolagemParser.PNomeAtividadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#listaComponentesAtividade.
    def visitListaComponentesAtividade(self, ctx:BricolagemParser.ListaComponentesAtividadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#componenteAtividade.
    def visitComponenteAtividade(self, ctx:BricolagemParser.ComponenteAtividadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#descricaoAtividade.
    def visitDescricaoAtividade(self, ctx:BricolagemParser.DescricaoAtividadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#duracaoAtividade.
    def visitDuracaoAtividade(self, ctx:BricolagemParser.DuracaoAtividadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#passosAtividade.
    def visitPassosAtividade(self, ctx:BricolagemParser.PassosAtividadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PPassoAtividade.
    def visitPPassoAtividade(self, ctx:BricolagemParser.PPassoAtividadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#avaliacaoProjeto.
    def visitAvaliacaoProjeto(self, ctx:BricolagemParser.AvaliacaoProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#listaComponentesAvaliacao.
    def visitListaComponentesAvaliacao(self, ctx:BricolagemParser.ListaComponentesAvaliacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#componenteAvaliacao.
    def visitComponenteAvaliacao(self, ctx:BricolagemParser.ComponenteAvaliacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#criteriosAvaliacao.
    def visitCriteriosAvaliacao(self, ctx:BricolagemParser.CriteriosAvaliacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PCriterioAvaliacao.
    def visitPCriterioAvaliacao(self, ctx:BricolagemParser.PCriterioAvaliacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#instrumentosAvaliacao.
    def visitInstrumentosAvaliacao(self, ctx:BricolagemParser.InstrumentosAvaliacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PInstrumentoAvaliacao.
    def visitPInstrumentoAvaliacao(self, ctx:BricolagemParser.PInstrumentoAvaliacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#recursosProjeto.
    def visitRecursosProjeto(self, ctx:BricolagemParser.RecursosProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PRecursoProjeto.
    def visitPRecursoProjeto(self, ctx:BricolagemParser.PRecursoProjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#conformidadeProjetoBNCC.
    def visitConformidadeProjetoBNCC(self, ctx:BricolagemParser.ConformidadeProjetoBNCCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BricolagemParser#PIDBNCCProjeto.
    def visitPIDBNCCProjeto(self, ctx:BricolagemParser.PIDBNCCProjetoContext):
        return self.visitChildren(ctx)



del BricolagemParser