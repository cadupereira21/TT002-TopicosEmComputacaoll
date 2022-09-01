# Aula 3 - Autor: Manko

print("Dicionários")

dados = {}
dados = dict()
dados = {"nome":"Pedro", "idade":20}
print(dados)

dados["sexo"] = "Masculino"
print(dados)

dados["nome"] = "Carlos"
print(dados)

del dados["sexo"]
print(dados)

mes = {
    "Jan":"Janeiro",
    "Fev":"Fevereiro",
    "Mar":"Março",
    "Abr":"Abril",
    "Mai":"Maio",
    "Jun":"Junho",
    "Jul":"Julho",
    "Ago":"Agosto",
    "Set":"Setembro",
    "Out":"Outubro",
    "Nov":"Novembro",
    "Dez":"Dezembro",
}

print(mes)

print(mes["Jan"])
print(mes.get("Mar"))
#print(mes("xus")) #KeyError
#print(mes.get("xyz")) #Retorna None, segundo parâmetro é mensagem para se retornar none

for key, value in mes.items():
    print(f"Chave: {key} | Valor: {value}")

print("\nLoja de filmes")
locadora = []
filme = {
    "titulo" : "Vingadores",
    "ano":"2012",
    "diretor":"Jose Qhedon"
}

filme2 = {
    "titulo":"Matrix",
    "ano":"1999",
    "diretor":"Wachowski"
    }

filme3 = {
    "titulo":"Kung Fu Panda",
    "ano":"2010",
    "diretor":"Ximbas"
}
locadora.append(filme)

print(locadora)

locadora.append(filme2)
print(locadora)
locadora.append(filme3)
print(locadora)
print(locadora[0]["titulo"])
print("\n----------------------------- \n")
print("\nGeografia\n")

'''
estado = {}
brasil = []
for c in range(0, 3):
    estado["uf"] = input("Digite UF: ")
    estado["sigla"] = input("Digite sigla: ")
    brasil.append(estado)
print(brasil)
#Este código está errado

estado = {}
brasil = []
print()
for c in range(0, 3):
    estado["uf"] = input("Digite UF: ")
    estado["sigla"] = input("Digite sigla: ")
    brasil.append(estado.copy())
print(brasil)
'''

# Divisão em arquivos
print("\nDivisao de arquivos\n")
import bandas
print(bandas.bandas[0])