pessoas = []
index = 0
while index < 3:
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    nascimento = input("Digite a data de nascimento: ")
    pessoa = {"nome":nome,"cpf":cpf, "nascimento":nascimento}
    pessoas.append(pessoa)
    index+=1

def showPessoas(pessoas):
    i = 1
    for p in pessoas:
        print(f"Pessoa {i}->"+
        f"Nome: {p['nome']} " +
        f"CPF: {p['cpf']} " +
        f"Nascimento: {p['nascimento']}")
        i+=1

#showPessoas(pessoas)