from Coordenada import Coordenada

class Rota:
    coordenadas = []

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

    def comprimento(self):
        totalDistance = 0

        for i in range(1, len(self.coordenadas)):
            totalDistance += self.coordenadas[i].distancia(self.coordenadas[i-1])
        totalDistance += self.coordenadas[i].distancia(self.coordenadas[-0])

        return totalDistance

    def copy(self):
        return Rota()