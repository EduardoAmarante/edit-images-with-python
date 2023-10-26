import os
import sys
from pathlib import Path
from time import sleep
from PIL import Image, ImageFont, ImageDraw


def photo_square_newvideo():
    b = Image.open("backgrounds/fundo_blue.png")
    r = Image.open("backgrounds/fundo_red.png")
    g = Image.open("backgrounds/fundo_green.png")
    pink = Image.open("backgrounds/fundo_pink.png")

    path = Path(os.path.abspath(os.path.dirname(sys.argv[0])))

    color = input("Digite blue/red/green/pink: ")

    for filename in path.glob('*'):
        try:
            if ("jpg" or "JPG") in str(filename):

                thumb_jpg = Image.open(filename)

                thumb_jpg = thumb_jpg.resize((1080, 608), Image.ADAPTIVE)

                if color == "red":
                    background = r.copy()
                elif color == "green":
                    background = g.copy()
                elif color == "pink":
                    background = pink.copy()
                elif color == "blue":
                    background = b.copy()

                background.paste(thumb_jpg, (0, 236))

                titulo = (str(filename)[str(filename).rfind('\\') + 1:]).replace(".jpg", ".png")

                background.save(str(path) + "/" + titulo)
                background.close()
        except Exception as e:
            s = str(e)
            sleep(10)


def thumb_maker(photo_filename, number):
    try:
        thumb = Image.open(photo_filename)
        # [Shadow, main color]
        cor = [(0, 0, 0), (71, 164, 191)]

        for i in range(2):
            title_font = ImageFont.truetype('font/LuckiestGuy-Regular.ttf', 390)
            if number > 9:
                title_text = "#{}".format(number)
            else:
                title_text = "#0{}".format(number)

            image_editable = ImageDraw.Draw(thumb)

            if i > 0:
                image_editable.text((1120, 600), title_text, cor[i], font=title_font)
                thumb.save("capa {}.jpg".format(number))
            else:
                image_editable.text((1150, 605), title_text, cor[i], font=title_font)
                thumb.save("capa {}.jpg".format(number))
    except FileNotFoundError:
        print("File {} not found in folder".format(photo_filename))
    except Exception as e:
        print("A exception happens when try to open {} image.".format(photo_filename))
        print(e)

for i in range(1, 15):
    thumb_maker('capa2.jpg', i)
