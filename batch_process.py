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


def thumb_maker(photo_filename, episode_number, accent_color='#47A4BF'):
    try:
        accent_color = accent_color.lstrip('#')
        thumb = Image.open(photo_filename)
        # [Shadow, main color]
        color = [(0, 0, 0), tuple(int(accent_color[i:i+2], 16) for i in (0, 2, 4))]
        title_message = "#{:02d}".format(episode_number)

        title_font = ImageFont.truetype('font/LuckiestGuy-Regular.ttf', 390)
        image_editable = ImageDraw.Draw(thumb)
        image_editable.text((1120, 600), title_message, color[0], font=title_font)
        image_editable.text((1150, 605), title_message, color[1], font=title_font)

        filename_without_ext = os.path.splitext(photo_filename)[0]
        output_file = "cover_{}_{}.jpg".format(filename_without_ext, episode_number)
        try:
            thumb.save(output_file)
        except Exception as err:
            print("Error on saving {}".format(output_file))
            print(err)
    except FileNotFoundError:
        print("File {} not found in folder".format(photo_filename))
    except Exception as err:
        print("A exception happens when try to open {} image.".format(photo_filename))
        print(err)