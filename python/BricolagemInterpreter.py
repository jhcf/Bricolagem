from antlr4 import *
from BricolagemLexer import BricolagemLexer
from BricolagemParser import BricolagemParser
from BricolagemParserVisitor import BricolagemParserVisitor
import os


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
    visitor.visit(tree)

    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main()
