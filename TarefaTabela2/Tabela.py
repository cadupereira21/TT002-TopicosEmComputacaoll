'''
AUTORES:

Carlos Eduardo de Andrade Pereira - 168321
Luiz Otávio de Oliveira Silva - 240519
Pedro Augusto Canuto de Oliveira - 186691
'''

from typing import List
from Linha import Linha
class Tabela:

    # TODO:
    # 1) (CHECK) Implementar construtor com argumento do tipo arquivo. O arquivo que será passado será no modelo de carros.txt
    # 2) (CHECK) Método writeFile(nomeArquivo) para salvar tabela em um arquivo

    def __init__(self, file=""):
        if(file == ""):
            self.dados = []
            self.cabecalho = Linha()
            return

        self.file = open(file)
        self.cabecalho = Linha(self.file.readline())
        self.dados = self.file.readlines()
        self.file.close()

    def add_cabecalho(self,valor):
        return self.cabecalho.append(valor)  

    def addLinha(self,linha):
        
        if len(linha.dados) == len(self.cabecalho.dados):
            self.dados.append(linha.dados)
        else:
            print("tamanho da linha incompatível")

    def ordena_por(self, filtro):
        for i in range(0, len(self.dados)-1):
            if self.dados[i][self.cabecalho.IndexOf(filtro)] > self.dados[i+1][self.cabecalho.IndexOf(filtro)]:
                aux = self.dados[i+1]
                self.dados[i+1] = self.dados[i]
                self.dados[i] = aux

    def writeFile(self, fileName):
        file = open(fileName, "w")
        file.write(str(self.cabecalho)+'\n')
        file.writelines(self.dados)
        file.close()

    
    def __str__(self):
        aux = str(self.cabecalho) + "\n"

        for s in self.dados:
            aux += str(s)
        return aux