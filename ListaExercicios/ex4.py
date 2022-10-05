def readCars(fileName):
    file = open(fileName, "r")
    cars = []
    for line in file.readlines():
        line = line.replace("{", "").replace("}", "").replace("\n", "").replace("\'", "")
        data = line.split(",")
        car = {"Marca":data[0].split(":")[1],
        "Modelo":data[1].split(":")[1],
        "Placa":data[2].split(":")[1]}
        cars.append(car)
    file.close()
    return cars

print(readCars("carros.txt"))