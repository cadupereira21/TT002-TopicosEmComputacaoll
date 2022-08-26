import sys


print("\nVersao Python")
print(sys.version + "\n")
print("Info")
print(sys.version_info)

#string
nome = "carlos"
#numero
idade = 20
altura = 1.70
print("\nNome -> " + nome)
print("Idade -> " + str(idade))
print(f"Altura -> {altura}")

#boolean
isMasculino = True

print("\n"+nome.upper())
print(len(nome))
print(nome[0]+nome[2]+nome[-1])
print(nome.index("c"))
print(nome)
print(nome.replace("arlos","lara"))

#funcoes matematicas
from math import *
print()
print(pow(2, 10))
print(max(1, 2, 3, 4, 5))
print(round(5.9))
print(floor(3.9))
print(ceil(3.9))

#listas
print("\nListas")
amigos = ["Paulo", 2, True]
amigos = ["Paulo", "Andre", "Joao"]
numeros = [4, 2, 6, 46, 8]
print(amigos[0])
print(numeros[-1])
amigos.extend(numeros)
print(amigos)
amigos.append("Rafael")
print(amigos)
amigos.insert(1, "Matheus")
amigos.insert(1, "Matheus")
print(amigos)
amigos.remove("Matheus")
print(amigos)
amigos.pop()
print(amigos)
amigos.append("Matheus")
print(amigos)
print(amigos.index("Matheus"))
print(amigos.count("Matheus"))

nova = amigos
nova.pop()
print(amigos)
print(nova)

print(amigos)
nova = amigos.copy()
nova.pop()
print(amigos)
print(nova)

#Tuplas - Listas que não podem ser alteradas
print("\nTuplas")
coordenada = (4, 3, 5)
print(coordenada[2])
# coordenada[0] = 4 (Não é possível)
print(coordenada)

#Sublistas
print("\nSublistas")
n_sorte = [56, 3, 8, 2, 45, 7, 3, 5, 1, 0]
print(n_sorte[1:])
print(n_sorte[1:2])
print(n_sorte[1:3])
print(n_sorte[1:4])

#funcoes em python
print("\nFunções")
def SayHello():
    print("Hello World!")

def ReturnHello():
    return "Hello!"

def Cubo(n):
    return n*n*n

SayHello()
ReturnHello() # Não printa
print(ReturnHello())
print(Cubo(3))
# print(Cubo("a"))  (Erro)

#condiçoes
print("\nCondicoes")
isTall = False
jumpsHigh = False
if isTall:
    print("eh alto")
else:
    print("nao eh alto")

if isTall and jumpsHigh:
    print("Joga basquete")
elif isTall and not jumpsHigh:
    print("Consegue jogar basquete")
else:
    print("Nao consegue jogar basquete")
