from PIL import Image

#img = Image.open("github-logo.png")

#img.show()

#img.save("github2.png")

#converter para jpeg
#img.save("github.png")

#descobrir
#print(img.size)

#img_resized = img.resize((30,30))
#img_resized.save("small.png")

#img.rotate(45).show()
#img.rotate(45,expand=True).show()
#img.rotate(90).show()
#img.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()
#img.transpose(Image.Transpose.FLIP_TOP_BOTTOM).show()
#img.transpose(Image.Transpose.ROTATE_180).show()

#numero de cores 256^3=16777216

#img.show()
largura = 300
altura = 200
img = Image.new('RGB',(largura,altura),(255,255,255))
pixeis = img.load()

R = 200
G = 200
B = 200

cor = (R,G,B)

img.show()