'''
AUTORES:

Carlos Eduardo de Andrade Pereira - 168321
Luiz Otávio de Oliveira Silva - 240519
Pedro Augusto Canuto de Oliveira - 186691
'''

class Linha:
    
    def __init__(self, line = ""):
        self.dados = []
        if(line == ""):
            return

        line = line.replace("[", "").replace("]", "").replace("\n", "")
        data = line.split(",")
        for d in data:
            self.dados.append(d)
        

    def __str__(self):
        num = 0
        lista = "["
        for num in range(0, len(self.dados)):
            if num == len(self.dados)-1:
                lista += f"{self.dados[num]}]"
                return lista
            lista += f"{self.dados[num]}, "
        return lista

    def __len__(self):
        return len(self.dados)

    def append(self, obj):
        if type(obj) is list:
            self.dados.extend(obj)
            return

        self.dados.append(obj)
        return

    def IndexOf(self, value):
        return self.dados.index(value)
    
f = open("carros.txt", "r")
linha = Linha(f.readline())
