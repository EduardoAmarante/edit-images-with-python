from pathlib import Path
from time import sleep
from PIL import Image
import os,sys

b = Image.open("./fundo_blue.png")
r = Image.open("./fundo_red.png")
g = Image.open("./fundo_green.png")
pink = Image.open("./fundo_pink.png")

path = Path(os.path.abspath(os.path.dirname(sys.argv[0])))

color = input("Digite blue/red/green/pink: ")

for filename  in path.glob('*'):
    try:
        if ("jpg" or "JPG") in str(filename):

            thumb_jpg = Image.open(filename)

            thumb_jpg = thumb_jpg.resize((1080,608),Image.ADAPTIVE)

            if color == "red":
                background = r.copy()
            elif color == "green":
                background = g.copy()
            elif color == "pink":
                background = pink.copy()
            elif color == "blue":
                background = b.copy()

            background.paste(thumb_jpg,(0, 236))

            titulo = (str(filename)[str(filename).rfind('\\')+1:]).replace(".jpg",".png")

            background.save(str(path) + "/" + titulo)
            background.close()
    except Exception as e:
        s = str(e)
        sleep(10)