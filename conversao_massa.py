from pathlib import Path
from PIL import Image

b = Image.open("./fundo_blue.png")
r = Image.open("./fundo_red.png")

path = Path("C:/Users/Eduardo/Desktop/script_imagens")

for filename  in path.glob('*'):

    if ("jpg" or "JPG") in str(filename):
        
    
        thumb_jpg = Image.open(filename)

        thumb_jpg = thumb_jpg.resize((1080,608),Image.ADAPTIVE)

        color = input("Digite blue ou red: ")
        try:
            if color == "red":
                background = r.copy()
            else:
                background = b.copy()
        except:
            print('erro')

        background.paste(thumb_jpg,(0, 236))

        titulo = ((str(filename).split("\\"))[5]).replace(".jpg",".png")
        
        background.save(str(path)+"/editados/{}".format(titulo))