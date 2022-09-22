from ast import List


class Linha:

    def __init__(self):
        self.dados = []

    def __str__(self):
        num = 0
        lista = "["
        for num in range(0, len(self.dados)):
            if num == len(self.dados)-1:
                lista += f"{self.dados[num]}]({len(self)})"
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
    