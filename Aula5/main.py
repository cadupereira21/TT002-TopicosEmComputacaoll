from PIL import Image

img = Image.open("github.jpg")

#img.show()

img.save("github2.jpg")

img.save("github.png") # Convertendo pra PNG

print(img.size) # Printa o tamanho para a imagem

img_resized = img.resize((65, 65))
img_resized.save("smallGithub.jpg")

#img.rotate(45).show() # Rotaciona a imagem em 45º

#img.transpose(Image.Transpose.FLIP_TOP_BOTTOM).show() # Espelha a imagem
#img.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show() # Espelha a imagem

pixels = img_resized.load()

R = 0
G = 0
B = 0

cor = (R, G, B)
pixels(10, 10) = cor


largura = 1000
altura = 500
img = Image.new('RGB', (largura, altura), (255,255,255)) # Cria uma imagem com fundo branco

#img.show()
