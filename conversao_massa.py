from pathlib import Path
from PIL import Image

b = Image.open("./fundo_blue.png")
r = Image.open("./fundo_red.png")
g = Image.open("./fundo_green.png")
pink = Image.open("./fundo_pink.png")

path = Path("C:/Users/Eduardo/Desktop/script_imagens")

color = input("Digite blue/red/green/pink: ")

for filename  in path.glob('*'):

    if ("jpg" or "JPG") in str(filename):

        thumb_jpg = Image.open(filename)

        thumb_jpg = thumb_jpg.resize((1080,608),Image.ADAPTIVE)

        if color == "red":
            background = r.copy()
        elif color == "green":
            background = g.copy()
        elif color == "pink":
            background = pink.copy()
        else:
            background = b.copy()

        background.paste(thumb_jpg,(0, 236))

        titulo = ((str(filename).split("\\"))[5]).replace(".jpg",".png")

        background.save(str(path) + "/editados/{}" .format(titulo))