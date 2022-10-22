import math
import random
from time import time
from Coordenada import Coordenada

class Rota:
    def __init__(self):
        self.coordenadas = []

    def __str__(self):
        if len(self.coordenadas) == 0:
            return ""

        aux = f"{self.coordenadas[0]}"
        for i in range(1, len(self.coordenadas)):
            aux += f"->{self.coordenadas[i]}"
        aux+=f"->{self.coordenadas[0]}"

        return aux

    def addCoord(self, coord):
        self.coordenadas.append(coord)

    def switchCoord(self, target, destiny):
        if target == destiny:
            return
        aux = self.coordenadas[target]
        self.coordenadas[target] = self.coordenadas[destiny]
        self.coordenadas[destiny] = aux

    def comprimento(self):
        totalDistance = 0

        for i in range(1, len(self.coordenadas)):
            totalDistance += self.coordenadas[i].distancia(self.coordenadas[i-1])
        totalDistance += self.coordenadas[i].distancia(self.coordenadas[-0])

        return totalDistance

    def copy(self):
        aux = Rota()

        for c in self.coordenadas.copy():
            aux.addCoord(c)
        
        return aux

    def shuffle(self):
        random.shuffle(self.coordenadas)

    def otimiza(self):
        actualComprimento = self.comprimento()
        for i in range(len(self.coordenadas)-1):
            lowestDistance = self.coordenadas[i].distancia(self.coordenadas[i+1])
            for j in range(i+2, len(self.coordenadas)):
                aux = i+1
                if self.coordenadas[i].distancia(self.coordenadas[j]) < lowestDistance:
                    aux = j
            self.switchCoord(i+1, aux)
        
        if actualComprimento < self.comprimento():
            self.otimiza()
        else:
            return

    def espera(self, dt):
        timestamp = time()*1000
        delta = 0
        secondsPassed = -1
        while(delta < dt):
            if(math.floor(delta/1000) > secondsPassed):
                print(f"Esperando : {(secondsPassed+1)*1000}")
                secondsPassed+=1
            delta = (time()*1000)-timestamp      
        return
              
                