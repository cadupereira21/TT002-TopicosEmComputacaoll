cars = []
i = 0
while i < 3:
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    placa = input("Digite a placa: ")
    carro = {"Marca":marca, "Modelo":modelo, "Placa":placa}
    cars.append(carro)
    i+=1

#print(cars)