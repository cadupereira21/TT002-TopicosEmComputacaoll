from Rota import Rota

rota = Rota()
n = 8
max_coord = 400
rota.randomCoords(n, max_coord)
print(rota)
print(rota.maximo())