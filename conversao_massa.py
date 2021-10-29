from pathlib import Path
from PIL import Image, ImageChops, ImageFilter
from matplotlib import image, pyplot as plt
from datetime import datetime

b = Image.open("./fundo_blue.png")
r = Image.open("./fundo_red.png")
#t = Image.open("./thumb.jpg")

path = Path("C:/Users/Eduardo/Desktop/script_imagens")

for filename  in path.glob('*'):

    if ("jpg" or "JPG") in str(filename):
        
    
        t = Image.open(filename)

        t = t.resize((1080,608),Image.ADAPTIVE)

        cor = "blue"

        if cor == "red":
            back = r.copy()
        else:
            back = b.copy()


        back.paste(t,(0, 236))

        titulo = ((str(filename).split("\\"))[5]).replace(".jpg",".png")
        
        back.save(str(path)+"/editados/{}".format(titulo))