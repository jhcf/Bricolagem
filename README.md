# Linguagem de programação DSL (Domain Specific Language) para planejamento de práticas pedagógicas maker.

Criada com ANTLR4

O arquivo python/RS.B é um exemplo de programa escrito na linguagem, que por enquanto é apenas declarativa.

Para usar execute, no diretório python, informando "RS.B":
  > python3 BricolagemInterpreter.py

Após atualizar o lexer, no diretório raiz do projeto, gere novas versões desses módulos
> java -jar ~/antlr-4.13.2-complete.jar -Dlanguage=Python3 BricolagemLexer.g4
> java -jar ~/antlr-4.13.2-complete.jar -visitor -listener -Dlanguage=Python3 BricolagemParser.g4 

Perceba que o código python do BricolagemParserVisitor.py deve ser sobrescrito com cuidado, para que não perca o gerador de código.
