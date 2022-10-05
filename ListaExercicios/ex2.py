import ex1

def showCars(cars):
    index = 1
    for car in cars:
        print(f"Carro {index}->"+
        f"Marca: {car['Marca']} "+
        f"Modelo: {car['Modelo']} "+
        f"Placa: {car['Placa']}")
        index +=1

showCars(ex1.cars)
