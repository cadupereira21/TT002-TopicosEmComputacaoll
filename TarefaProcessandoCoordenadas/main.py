import geopy.distance
file = open("coordenadas.txt", "r")

while True:
    try:
        lat = float(input("Digite a latitude: "))
        lon = float(input("Digite a longitude: "))
        break
    except:
        print("Entre com um dado valido")

# Armazena os ultimos dois valores da linha em uma lista
line = file.readline().split(";")[-2:]
# transforma a lista em uma coordenada com floats
coord = (float(line[0]), float(line[1].replace("\n", "")))
lowestDistance = geopy.distance.geodesic((lat, lon), coord)
print(lowestDistance)