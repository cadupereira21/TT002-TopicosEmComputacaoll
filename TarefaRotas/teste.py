from Rota import Rota
from Coordenada import Coordenada

rota = Rota()
rota.addCoord(Coordenada((0, 0)))
rota.addCoord(Coordenada((300, 300)))
rota.addCoord(Coordenada((600, 0)))
filename = "rotaA.png"
rota.desenha(filename).show()