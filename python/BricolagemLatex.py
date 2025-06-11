from pylatex import Document, Section, Subsection, Command, Package, Itemize
from pylatex.utils import NoEscape
from datetime import datetime
from typing import List, Tuple, Dict
import os

class BricolagemLatex:
    def __init__(self, file:str, path:str):
        self.file = file
        self.doc = Document()
        self.doc.packages.remove(Package('lastpage'))
        self.path = path

    def title(self, title:str, subtitle:str):
        capaImagePath = self.path+'/img/capa.png'
        self.doc.packages.append(Package('graphicx'))
        self.doc.preamble.append(Command('title', NoEscape(f'{title} \\\\[1ex] \\large {subtitle}')))
        self.doc.append(NoEscape(r'\maketitle'))
        self.doc.append(NoEscape(r'\thispagestyle{empty}'))
        self.doc.append(NoEscape(r'\centering'))
        self.doc.append(NoEscape(rf'\includegraphics[width=1.0\textwidth]{{{capaImagePath}}}'))
        self.doc.append(NoEscape(r'\newpage'))
        return self
    
    def author(self, author:str):
        self.doc.preamble.append(Command('author', author))
        return self
    
    def date(self):
        self.doc.preamble.append(Command('date', NoEscape(datetime.now().strftime(r'%d/%m/%Y'))))
        return self
    
    def objetivoEnsino(self, objetivoEnsino:List[Tuple[str,str]]):
        with self.doc.create(Section("Objetivo de Ensino")):
            for subsection in objetivoEnsino:
                with self.doc.create(Subsection(subsection[0])):
                    self.doc.append(subsection[1])
        return self
    
    def objetivoAprendizagem(self, objetivoAprendizagem:List[Tuple[str,str]]):
        with self.doc.create(Section("Objetivo de Aprendizagem")):
            for subsection in objetivoAprendizagem:
                with self.doc.create(Subsection(subsection[0])):
                    self.doc.append(subsection[1])
        return self
    
    def objetivoPesquisa(self, objetivoPesquisa:List[Tuple[str,str]]):
        with self.doc.create(Section("Objetivo de Pesquisa")):
            for subsection in objetivoPesquisa:
                with self.doc.create(Subsection(subsection[0])):
                    self.doc.append(subsection[1])    
        return self
    
    def objetivoEducacional(self, objetivoEducacional:List[Tuple[str,str]]):
        with self.doc.create(Section("Objetivo Educacional")):
            for subsection in objetivoEducacional:
                with self.doc.create(Subsection(subsection[0])):
                    self.doc.append(subsection[1])   
        return self
    
    def atividade(self, atividades:List[Dict[str, Dict[str, str | List[str]]]]):
        with self.doc.create(Section("Atividades")):
            for atividade in atividades:
                for name in atividade.keys():
                    with self.doc.create(Subsection(name)):
                        descricao = atividade[name]["Descricao"]
                        duracao = atividade[name]["DuracaoMinutos"]
                        passos = atividade[name]["Passos"]
                        self.doc.append(NoEscape(f'{descricao} \\\\ Duração: {duracao} minutos \\\\'))
                        self.doc.append(NoEscape(r'\textbf{Passos:} \\'))
                        self.doc.append(NoEscape(r'\vspace{-5mm}'))  
                        with self.doc.create(Itemize()) as list:
                            for passo in passos:
                                list.add_item(passo)
        return self
    
    def avaliacao(self, avaliacao:List[Tuple[str,List[str]]]):
        with self.doc.create(Section("Avaliação")):
            for subsection in avaliacao:
                with self.doc.create(Subsection(subsection[0])):
                    with self.doc.create(Itemize()) as list:
                        for item in subsection[1]:
                            list.add_item(item)
        return self
    
    def recurso(self, recurso:List[str]):
        with self.doc.create(Section("Recursos")):
            with self.doc.create(Itemize()) as list:
                for item in recurso:
                    list.add_item(item)
        return self
    
    def conformidadeBNCC(self, conformidadeBNCC:List[str]):
        with self.doc.create(Section("Conformidade BNCC")):
            with self.doc.create(Itemize()) as list:
                for item in conformidadeBNCC:
                    list.add_item(item)
        return self
    
    def build(self):
        os.makedirs(self.path+'/pdf/', exist_ok=True)
        os.makedirs(self.path+'/tex/', exist_ok=True)
        self.doc.generate_tex(self.path+'/tex/'+self.file)
        self.doc.generate_pdf(self.path+'/pdf/'+self.file)
        return self
    
    