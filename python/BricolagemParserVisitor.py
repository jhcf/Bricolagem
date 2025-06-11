from antlr4 import *
if "." in __name__:
    from .BricolagemParser import BricolagemParser
else:
    from BricolagemParser import BricolagemParser


class BricolagemParserVisitor(ParseTreeVisitor):

    def visitProjetoMaker(self, ctx:BricolagemParser.ProjetoMakerContext):
        return self.visit(ctx.listaElementos())

    def visitListaElementos(self, ctx:BricolagemParser.ListaElementosContext):
        return {
            key: value 
            for el in ctx.elemento() 
            if (result := self.visit(el)) is not None 
            and (key := result[0]) 
            and (value := result[1])
        }

    def visitPNivel(self, ctx:BricolagemParser.PNivelContext):
        nivel_ctx = ctx.nivel()
        key = nivel_ctx.NIVEL().getText()
        value = self.visitChildren(ctx)
        return (key, value)

    def visitPTema(self, ctx:BricolagemParser.PTemaContext):
        tema_ctx = ctx.tema()
        key = tema_ctx.TEMA().getText()
        value = self.visitChildren(ctx)
        return (key, value)

    def visitPObjetivosProjeto(self, ctx:BricolagemParser.PObjetivosProjetoContext):
        key = "ObjetivosProjeto"
        value = self.visitChildren(ctx)
        return (key, value)

    def visitPAtividadesProjeto(self, ctx:BricolagemParser.PAtividadesProjetoContext):
        atividades_ctx = ctx.atividadesProjeto()
        key = atividades_ctx.ATIVIDADES().getText()
        value = self.visitChildren(ctx)
        return (key, value)

    def visitPAvaliacaoProjeto(self, ctx:BricolagemParser.PAvaliacaoProjetoContext):
        avaliacao_ctx = ctx.avaliacaoProjeto()
        key = avaliacao_ctx.AVALIACAO().getText()
        value = self.visitChildren(ctx)
        return (key, value)

    def visitPRecursosProjeto(self, ctx:BricolagemParser.PRecursosProjetoContext):
        recursos_ctx = ctx.recursosProjeto()
        key = recursos_ctx.RECURSOS().getText()
        value = self.visitChildren(ctx)
        return (key, value)

    def visitPConformidadeProjetoBNCC(self, ctx:BricolagemParser.PConformidadeProjetoBNCCContext):
        conformidade_ctx = ctx.conformidadeProjetoBNCC()
        key = conformidade_ctx.CONFORMIDADE_BNCC().getText()
        value = self.visitChildren(ctx)
        return (key, value)

    def visitNivel(self, ctx:BricolagemParser.NivelContext):
        return ctx.STRING().getText().strip('"')

    def visitTema(self, ctx:BricolagemParser.TemaContext):
        return ctx.STRING().getText().strip('"')

    def visitObjetivosProjeto(self, ctx:BricolagemParser.ObjetivosProjetoContext):
        return [self.visit(objetivo) for objetivo in ctx.objetivo()]

    def visitPObjetivosEnsino(self, ctx:BricolagemParser.PObjetivosEnsinoContext):
        key = ctx.OBJETIVO_ENSINO().getText()
        value = self.visit(ctx.listaObjetivosEnsino())
        return {key: value}

    def visitPObjetivosAprendizagem(self, ctx:BricolagemParser.PObjetivosAprendizagemContext):
        key = ctx.OBJETIVO_APRENDIZAGEM().getText()
        value = self.visit(ctx.listaObjetivosAprendizagem())
        return {key: value}

    def visitPObjetivosPesquisa(self, ctx:BricolagemParser.PObjetivosPesquisaContext):
        key = ctx.OBJETIVO_PESQUISA().getText()
        value = self.visit(ctx.listaObjetivosPesquisa())
        return {key: value}


    def visitPObjetivosEducacionais(self, ctx:BricolagemParser.PObjetivosEducacionaisContext):
        key = ctx.OBJETIVO_EDUCACIONAL().getText()
        value = self.visit(ctx.listaObjetivosEducacionais())
        return {key: value}

    def visitListaObjetivosEnsino(self, ctx:BricolagemParser.ListaObjetivosEnsinoContext):
        return {
            key: value 
            for el in ctx.objetivoEnsino() 
            if (result := self.visit(el)) is not None 
            and (key := result[0]) 
            and (value := result[1])
        }

    def visitPObjetivoEnsino(self, ctx:BricolagemParser.PObjetivoEnsinoContext):
        key = self.visit(ctx.idObjetivoEnsino())
        value = self.visit(ctx.descricaoObjetivoEnsino())
        return (key, value)
    
    def visitIdObjetivoEnsino(self, ctx:BricolagemParser.IdObjetivoEnsinoContext):
        return ctx.getText().strip('"')

    def visitDescricaoObjetivoEnsino(self, ctx:BricolagemParser.DescricaoObjetivoEnsinoContext):
        return ctx.getText().strip('"')

    def visitListaObjetivosAprendizagem(self, ctx:BricolagemParser.ListaObjetivosAprendizagemContext):
        return {
            key: value 
            for el in ctx.objetivoAprendizagem() 
            if (result := self.visit(el)) is not None 
            and (key := result[0]) 
            and (value := result[1])
        }

    def visitPObjetivoAprendizagen(self, ctx:BricolagemParser.PObjetivoAprendizagenContext):
        key = self.visit(ctx.idObjetivoAprendizagem())
        value = self.visit(ctx.descricaoObjetivoAprendizagem())
        return (key, value)

    def visitIdObjetivoAprendizagem(self, ctx:BricolagemParser.IdObjetivoAprendizagemContext):
        return ctx.getText().strip('"')

    def visitDescricaoObjetivoAprendizagem(self, ctx:BricolagemParser.DescricaoObjetivoAprendizagemContext):
        return ctx.getText().strip('"')

    def visitListaObjetivosPesquisa(self, ctx:BricolagemParser.ListaObjetivosPesquisaContext):
        return {
            key: value 
            for el in ctx.objetivoPesquisa() 
            if (result := self.visit(el)) is not None 
            and (key := result[0]) 
            and (value := result[1])
        }

    def visitPObjetivoPesquisa(self, ctx:BricolagemParser.PObjetivoPesquisaContext):
        key = self.visit(ctx.idObjetivoPesquisa())
        value = self.visit(ctx.descricaoObjetivoPesquisa())
        return (key, value)

    def visitIdObjetivoPesquisa(self, ctx:BricolagemParser.IdObjetivoPesquisaContext):
        return ctx.getText().strip('"')

    def visitDescricaoObjetivoPesquisa(self, ctx:BricolagemParser.DescricaoObjetivoPesquisaContext):
        return ctx.getText().strip('"')

    def visitListaObjetivosEducacionais(self, ctx:BricolagemParser.ListaObjetivosEducacionaisContext):
        return {
            key: value 
            for el in ctx.objetivoEducacional() 
            if (result := self.visit(el)) is not None 
            and (key := result[0]) 
            and (value := result[1])
        }

    def visitPObjetivoEducacional(self, ctx:BricolagemParser.PObjetivoEducacionalContext):
        key = self.visit(ctx.idObjetivoEducacional())
        value = self.visit(ctx.descricaoObjetivoEducacional())
        return (key, value)

    def visitIdObjetivoEducacional(self, ctx:BricolagemParser.IdObjetivoEducacionalContext):
        return ctx.getText().strip('"')

    def visitDescricaoObjetivoEducacional(self, ctx:BricolagemParser.DescricaoObjetivoEducacionalContext):
        return ctx.getText().strip('"')

    def visitAtividadesProjeto(self, ctx:BricolagemParser.AtividadesProjetoContext):
        return self.visit(ctx.listaAtividades())

    def visitListaAtividades(self, ctx:BricolagemParser.ListaAtividadesContext):
        return [child for c in ctx.children if (child := self.visit(c)) is not None]

    def visitPAtividade(self, ctx:BricolagemParser.PAtividadeContext):
        key = ctx.nomeAtividade().getText().strip('"')
        value = self.visit(ctx.listaComponentesAtividade())
        return {key: value}

    def visitPNomeAtividade(self, ctx:BricolagemParser.PNomeAtividadeContext):
        return ctx.getText().strip('"')

    def visitListaComponentesAtividade(self, ctx:BricolagemParser.ListaComponentesAtividadeContext):
        return {
            key: value
            for el in ctx.componenteAtividade()
            if (result := self.visit(el)) is not None 
            and (key := result[0]) 
            and (value := result[1])
        }

    def visitComponenteAtividade(self, ctx:BricolagemParser.ComponenteAtividadeContext):
        return self.visitChildren(ctx)

    def visitDescricaoAtividade(self, ctx:BricolagemParser.DescricaoAtividadeContext):
        key = ctx.DESCRICAO().getText().strip('"')
        value = ctx.STRING().getText().strip('"')
        return (key, value)

    def visitDuracaoAtividade(self, ctx:BricolagemParser.DuracaoAtividadeContext):
        key = ctx.DURACAOMINUTOS().getText().strip('"')
        value = ctx.NUMERO().getText().strip('"')
        return (key, value)

    def visitPassosAtividade(self, ctx:BricolagemParser.PassosAtividadeContext):
        key = ctx.PASSOS().getText()
        value = [self.visit(passoAtividade) for passoAtividade in ctx.passoAtividade()]
        return (key, value)

    def visitPPassoAtividade(self, ctx:BricolagemParser.PPassoAtividadeContext):
        return ctx.getText().strip('"')

    def visitAvaliacaoProjeto(self, ctx:BricolagemParser.AvaliacaoProjetoContext):
        return self.visit(ctx.listaComponentesAvaliacao())

    def visitListaComponentesAvaliacao(self, ctx:BricolagemParser.ListaComponentesAvaliacaoContext):
        return {
            key: value
            for el in ctx.componenteAvaliacao()
            if (result := self.visit(el)) is not None 
            and (key := result[0]) 
            and (value := result[1])
        }

    def visitComponenteAvaliacao(self, ctx:BricolagemParser.ComponenteAvaliacaoContext):
        return self.visitChildren(ctx)

    def visitCriteriosAvaliacao(self, ctx:BricolagemParser.CriteriosAvaliacaoContext):
        key = ctx.CRITERIOS().getText()
        value = [self.visit(criterioAvaliacao) for criterioAvaliacao in ctx.criterioAvaliacao()]
        return (key, value)

    def visitPCriterioAvaliacao(self, ctx:BricolagemParser.PCriterioAvaliacaoContext):
        return ctx.getText().strip('"')

    def visitInstrumentosAvaliacao(self, ctx:BricolagemParser.InstrumentosAvaliacaoContext):
        key = ctx.INSTRUMENTOS().getText()
        value = [self.visit(instrumentoAvaliacao) for instrumentoAvaliacao in ctx.instrumentoAvaliacao()]
        return (key, value)

    def visitPInstrumentoAvaliacao(self, ctx:BricolagemParser.PInstrumentoAvaliacaoContext):
        return ctx.getText().strip('"')

    def visitRecursosProjeto(self, ctx:BricolagemParser.RecursosProjetoContext):
        return [self.visit(recurso) for recurso in ctx.recurso()]

    def visitPRecursoProjeto(self, ctx:BricolagemParser.PRecursoProjetoContext):
        return ctx.STRING().getText().strip('"')

    def visitConformidadeProjetoBNCC(self, ctx:BricolagemParser.ConformidadeProjetoBNCCContext):
        return [child for c in ctx.children if (child := self.visit(c)) is not None]

    def visitPIDBNCCProjeto(self, ctx:BricolagemParser.PIDBNCCProjetoContext):
        return ctx.getText().strip('"')

del BricolagemParser