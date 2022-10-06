
def compras(pessoas, carros, compras=[]):
    cpf = input("Digite cpf: ")
    placa = input("Digite placa: ")
    cpfExists = False
    placaExists = False

    for p in pessoas:
        if p['cpf'] == cpf:
            cpfExists = True

    for c in carros:
        if str(c['Placa']).lower() == str(placa).lower():
            placaExists = True

    if not cpfExists:
        print("CPF não encontrado")
        return compras
    if not placaExists:
        print("Carro não encontrado")
        return compras
    
    compras.append((cpf, placa))
    print("Compra efetuada com sucesso")
    return compras

pessoa = [{"nome":"Carlos","cpf":"51481893807", "nascimento":"21/01/2002"}]
car = [{"Marca":"Volkswagen", "Modelo":"Gol", "Placa":"ERP1234"}]

print(compras(pessoa, car))
