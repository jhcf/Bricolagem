from antlr4 import *
from BricolagemLexer import BricolagemLexer
from BricolagemParser import BricolagemParser
from BricolagemParserVisitor import BricolagemParserVisitor
from BricolagemLatex import BricolagemLatex
import os
from BricolagemOpenIA import gerar_imagem

def main():
    filename = input("Entre o nome do programa escrito na linguagem Bricolagem: ")
    with open(filename) as file:
        data = f'{file.read()}\n'

    input_stream = InputStream(data)
    lexer = BricolagemLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BricolagemParser(stream)
    tree = parser.projetoMaker()
    visitor = BricolagemParserVisitor()
    result = visitor.visit(tree)

    autor = input("Nome do author: ")

    tema = result["Tema"]
    nivel = result["Nivel"]
    objetivoEnsino = list(next((obj for obj in result["ObjetivosProjeto"] if obj and "ObjetivoEnsino" in obj.keys()), None)["ObjetivoEnsino"].items())
    objetivoAprendizagem = list(next((obj for obj in result["ObjetivosProjeto"] if obj and "ObjetivoAprendizagem" in obj.keys()), None)["ObjetivoAprendizagem"].items())
    objetivoPesquisa = list(next((obj for obj in result["ObjetivosProjeto"] if obj and "ObjetivoPesquisa" in obj.keys()), None)["ObjetivoPesquisa"].items())
    objetivoEducacional = list(next((obj for obj in result["ObjetivosProjeto"] if obj and "ObjetivoEducacional" in obj.keys()), None)["ObjetivoEducacional"].items())
    atividade = result["Atividades"]
    avaliacao = [(key, value)for (key, value) in result["Avaliacao"].items()]
    recurso = result["Recursos"]
    conformidadeBNCC = result["ConformidadeBNCC"]
    
    prompt = f"""
    Estou desenvolvendo um plano de aula e gostaria de adicionar uma imagem sobre "{tema}" utilizando os principios do Projeto Maker.
    O Tema da minha aula é "{tema}" e é para alunos do "{nivel}".
    As atividades que serão realizadas são: {", ".join([", ".join(list(a.keys())) for a in atividade])}.
    A imagem não pode conter textos e deve ter o estilo de um desenho.
    """

    imagemCapa = "capa.png"

    dir_atual = os.path.dirname(os.path.abspath(__file__))
    gerar_imagem(prompt,imagemCapa,dir_atual+"/out/img")

    (
        BricolagemLatex("file", dir_atual+"/out")
        .title(f"Projeto Maker - {tema}", nivel)
        .author(autor)
        .objetivoEnsino(objetivoEnsino)
        .objetivoAprendizagem(objetivoAprendizagem)
        .objetivoPesquisa(objetivoPesquisa)
        .objetivoEducacional(objetivoEducacional)
        .atividade(atividade)
        .avaliacao(avaliacao)
        .recurso(recurso)
        .conformidadeBNCC(conformidadeBNCC)
        .date()
        .build()
    )



if __name__ == '__main__':
    main()
