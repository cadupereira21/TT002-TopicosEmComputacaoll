'''
AUTORES:

Carlos Eduardo de Andrade Pereira - 168321
Luiz Otávio de Oliveira Silva - 240519
Pedro Augusto Canuto de Oliveira - 186691
'''

from Tabela import Tabela
from Linha import Linha

tab = Tabela()
tab.add_cabecalho(["Placa", "Ano", "Marca", "Modelo"])
carro = Linha()
carro.append(["ZBB1B11", 1998, "Ford", "Ka"])
tab.addLinha(carro)
carro = Linha()
carro.append(["BBB1B22", 2010, "Ford", "Fusion"])
tab.addLinha(carro)
carro = Linha()
carro.append(["DBB1B33", 2020, "Fiat", "Uno"])
tab.addLinha(carro)
carro = Linha()
carro.append(["CBB1B00", 2015, "Volks", "Gol"])
tab.addLinha(carro)

print(tab)

tab.ordena_por("Ano")
print(tab)

tab.ordena_por("Modelo")
print(tab)

tab.ordena_por("Placa")
print(tab)
