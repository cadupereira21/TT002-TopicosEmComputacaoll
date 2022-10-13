from distutils.log import error
from PIL import Image

'''
Função para normalizar um array, dado seu máximo e seu mínimo, em um range de 0 a 1000 (pixels da imagem)

Parâmetro
arr > Array a ser normalizado

Retorno
Um array com os valores de arr normalizado
'''
def Normalize(arr):
    norm_arr = []
    MIN = min(arr)
    MAX = max(arr)
    
    for i in arr:
        aux = (i+abs(MIN))*1000/(MAX+abs(MIN))
        norm_arr.append(aux)
    return norm_arr

'''
Função para pegar as coordenadas de uma linha do arquivpo

Parâmetros
s > string linha do arquivo

Retorno
lista com [longitude, latitude, estado] daquela linha
'''
def GetCoordenadasFromFileString(s):
    str(s).replace("\n", "")
    s = str(s).split(';')
    return [float(s[3]), float(s[4]), s[1]]

img = Image.new('RGB',(1001,1001),(255,255,255))

# Ler arquivo
file = open("coordenadas.txt", "r")
fileData = file.readlines()
file.close()

latitudes = []
longitudes = []
estados = []

# Pegando todas as latitudes e longitudes do arquivo
for d in fileData:
    d = GetCoordenadasFromFileString(d)
    longitudes.append(d[0])
    latitudes.append(d[1])
    estados.append(d[2])

# Normalizando os valores separadamente
normalized_lon = Normalize(longitudes)
normalized_lat = Normalize(latitudes)

# Salvando as coordenadas normalizadas
coordenadas = []
for i in range(0, len(longitudes)):
    coordenadas.append((round(normalized_lon[i]), round(normalized_lat[i])))

pixel = img.load()

cores = {
    "Acre":(0, 0, 0),
    "Roraima":(0, 0, 255),
    "Amazonas":(218,165,32),
    "Rondonia":(75,0,130),
    "Amapa":(128,0,0),
    "Para":(255,255,0),
    "Tocantins":(255,0,255),
    "Maranhao":(210,105,30),
    "Piaui":(0,255,0),
    "Bahia":(0,255,255),
    "Ceara":(0,0,128),
    "Rio Grande do Norte":(105,105,105),
    "Paraiba":(85,107,47),
    "Pernambuco":(255,69,0),
    "Alagoas":(70,130,180),
    "Sergipe":(0,100,0),
    "Mato Grosso":(139,69,19),
    "Mato Grosso do Sul":(148,0,211),
    "NA":(255,0,0),
    "Goias":(255,0,0),
    "Minas Gerais":(0,128,128),
    "Espirito Santo":(128,128,0),
    "Rio de Janeiro":(139,0,0),
    "Sao Paulo":(64,224,208),
    "Parana":(34,139,34),
    "Santa Catarina":(139,0,139),
    "Rio Grande do Sul":(178,34,34),
    "Distrito Federal":(60,179,113)
}

for i in range(0, len(coordenadas)):
    pixel[coordenadas[i][0], coordenadas[i][1]] = cores[estados[i]]


img.rotate(90).save("Brasil.png")

