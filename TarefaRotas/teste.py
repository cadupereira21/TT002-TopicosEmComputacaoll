from Rota import Rota
from Coordenada import Coordenada

rota = Rota()
n = 10
max_coord = 400
rota.randomCoords(n, max_coord)
rota.desenha("rota10.png").show()
# implementar uma função de otimização
rota.otimiza()
rota.desenha("rota10_Otimizada.png").show()
