import math
import random
from time import time
from Coordenada import Coordenada
from PIL import Image, ImageDraw

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

    def randomCoords(self, n, maxCoords):
        for i in range(n):
            x = random.randrange(1, maxCoords)
            y = random.randrange(1, maxCoords)
            self.addCoord(Coordenada((x,y)))
        return

    def maximo(self):
        xMax = self.coordenadas[0].x
        yMax = self.coordenadas[0].y
        
        for c in self.coordenadas:
            if c.x > xMax:
                xMax = c.x
            if c.y > yMax:
                yMax = c.y
        
        return (xMax, yMax)

    def desenha(self, fp):

        routeSize = self.maximo()
        constX = (routeSize[0]*0.1)/2
        constY = (routeSize[1])/2

        img = Image.new('RGB',(math.ceil(routeSize[0]*1.1), math.ceil(routeSize[1]*1.6)),(255,255,255))
        pixels = img.load()

        for c in self.coordenadas:
            pixels[c.x +constX, c.y +constY] = (0,0,0)

        for i in range(len(self.coordenadas)):
            coord1 = (self.coordenadas[i].x+constX, self.coordenadas[i].y+constY)
            if i+1 != len(self.coordenadas):
                coord2 = (self.coordenadas[i+1].x+constX, self.coordenadas[i+1].y+constY)
            else:
                coord2 = (self.coordenadas[0].x+constX, self.coordenadas[0].y+constY)
            shape = [coord1, coord2] 
            img1 = ImageDraw.Draw(img)   
            img1.line(shape, fill ="black", width = 2) 

        #TODO: Escrever comprimento

        img.transpose(method=Image.FLIP_TOP_BOTTOM).save(fp)

        return img.transpose(method=Image.FLIP_TOP_BOTTOM)