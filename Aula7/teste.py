import random
from Coordenada import Coordenada
from Rota import Rota
'''
rota1 = Rota()
for i in range(50):
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)
    cord = Coordenada((x, y))
    rota1.addCoord(cord)
'''
rota1 = Rota()

rota1.addCoord(Coordenada((0,0)))
rota1.addCoord(Coordenada((0,4)))
rota1.addCoord(Coordenada((3,0)))
rota1.addCoord(Coordenada((3,4)))

print(rota1)
print(rota1.comprimento())
print()

rota1.otimiza()
print(rota1)
print(rota1.comprimento())