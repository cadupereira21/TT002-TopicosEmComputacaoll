import ex1
file = open("carros.txt", "w")
for car in ex1.cars:
    file.write(str(car)+"\n")
file.close()
    