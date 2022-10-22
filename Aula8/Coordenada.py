import math
import Coordenada

class Coordenada:
    def __init__(self, *args):
        if len(args) != 1:
            raise Exception(f"Numero de argumentos errado: {len(args)}")
        if type(args[0]) is not tuple:
            raise Exception("Parâmetro não é uma tupla")
        if len(args[0]) != 2:
            raise Exception(f"Numero de coordenadas inválido: {len(args[0])}")
        for n in args[0]:
            if type(n) is not int and type(n) is not float:
                raise Exception("Elemento da tupla não é int or float")

        self.x = args[0][0]
        self.y = args[0][1]

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distancia(self, coord:Coordenada):
        xDiff = abs(self.x-coord.x)
        yDiff = abs(self.y-coord.y)
        
        return math.sqrt(math.pow(xDiff, 2) + math.pow(yDiff, 2))

