from PIL import Image

# explicit function to normalize array
def Normalize(arr):
    norm_arr = []
    MIN = min(arr)
    MAX = max(arr)
    
    for i in arr:
        aux = (i+abs(MIN))*1000/(MAX+abs(MIN))
        norm_arr.append(aux)
    return norm_arr

def GetCoordenadasFromFileString(s):
    str(s).replace("\n", "")
    s = str(s).split(';')
    return [float(s[3]), float(s[4])]

img = Image.new('RGB',(1001,1001),(255,255,255))

file = open("coordenadas.txt", "r")
fileData = file.readlines()
file.close()

latitudes = []
longitudes = []

# Pegando todas as latitudes e longitudes do arquivo
for d in fileData:
    d = GetCoordenadasFromFileString(d)
    longitudes.append(d[0])
    latitudes.append(d[1])

# Normalizando os valores separadamente
normalized_lon = Normalize(longitudes)
normalized_lat = Normalize(latitudes)

# Salvando as coordenadas normalizadas
coordenadas = []
for i in range(0, len(longitudes)):
    coordenadas.append((round(normalized_lon[i]), round(normalized_lat[i])))

preto = (0, 0, 0)
pixel = img.load()

for c in coordenadas:
    pixel[c[0], c[1]] = preto

img.save("Brasil.png")