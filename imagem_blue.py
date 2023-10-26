from PIL import Image, ImageChops, ImageFilter
from matplotlib import image, pyplot as plt


b = Image.open("backgrounds/fundo_blue.png")
#r = Image.open("./fundo_red.png")
t = Image.open("./thumb.jpg")

t = t.resize((1080,608),Image.ADAPTIVE)

cor = "blue"

if cor == "red":
    back = r.copy()
else:
    back = b.copy()
back.paste(t,(0, 236))
back.save("video_novo.png")