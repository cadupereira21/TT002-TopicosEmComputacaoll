import geopy.distance
def GeoDistance(coord1, coord2):
    try:
        distance = geopy.distance.geodesic(coord1, coord2)
        return distance
    except:
        return -1

def TransformLineInCoord(textLine):
    try:
        line = textLine.split(";")[-2:]
        linhaCoord = (float(line[0]), float(line[1].replace("\n", "")))
        return linhaCoord
    except ValueError as err:
        return err

def SearchClosestPlace(listOfLocations, myLocation):
  closestPlace = listOfLocations[0]
  line = closestPlace.split(";")[-2:]
  coord = (float(line[0]), float(line[1].replace("\n", "")))
  lowestDistance = geopy.distance.geodesic(myCoord, coord)

  for linha in listOfLocations:
    distance = GeoDistance(myLocation, TransformLineInCoord(linha))
      
    if distance < lowestDistance:
      lowestDistance = distance
      closestPlace = linha
  file.close()    
  return closestPlace

# ----------------------------------------------------

file = open("coordenadas.txt", "r")

while True:
    try:
        lat = float(input("Digite a latitude: "))
        lon = float(input("Digite a longitude: "))
        break
    except:
        print("Entre com um dado valido")

myCoord = (lat, lon)

print(SearchClosestPlace(file.readlines(), myCoord))