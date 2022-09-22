'''
AUTORES:

Carlos Eduardo de Andrade Pereira - 168321
Luiz Otávio de Oliveira Silva - 240519
Pedro Augusto Canuto de Oliveira - 186691
'''

from Linha import Linha

aux = Linha()
# o parâmetro é uma lista
aux.append([1, 2, 3, 4, 3])
# o parâmetro não é uma lista
aux.append(2)

print(str(aux))
print("Comprimento:"+str(len(aux)))