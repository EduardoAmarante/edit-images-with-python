from PIL import Image, ImageChops, ImageFilter
from matplotlib import image, pyplot as plt


b = Image.open("./fundo_blue.png")
r = Image.open("./fundo_red.png")
t = Image.open("./thumb.png")

t = t.resize((1080,608),Image.ADAPTIVE)

cor = "red"

if cor == "red":
    back = r.copy()
else:
    back = b.copy()
back.paste(t,(0, 236))
back.save("video_novo.png")