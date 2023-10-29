import os
import sys
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw
import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--color', type=click.Choice(['red', 'blue', 'green', 'pink'], case_sensitive=False),
              default='red', help='Set the color of background')
def square_photo_new_video(color):
    """
    Performs batch processing of multiple images to square photo format
    """
    try:
        blue_background = Image.open("backgrounds/bg_blue.png")
        red_background = Image.open("backgrounds/bg_red.png")
        green_background = Image.open("backgrounds/bg_green.png")
        pink_background = Image.open("backgrounds/bg_pink.png")
    except FileNotFoundError as err:
        print("File not found in folder")
        print(err)
        exit(1)
    except Exception as err:
        print("An exception occurred when open background files.")
        print(err)
        exit(1)

    background_mapped = {
        'blue': blue_background,
        'red': red_background,
        'green': green_background,
        'pink': pink_background
    }

    current_path = Path(os.path.abspath(os.path.dirname(sys.argv[0])))
    for filename in current_path.glob('*.jpg'):
        try:
            thumb_jpg = Image.open(filename).resize((1080, 608), Image.ADAPTIVE)
            if background_mapped.get(color) is None:
                background = blue_background.copy()
            else:
                background = background_mapped.get(color).copy()
            background.paste(thumb_jpg, (0, 236))

            titled_thumbnail = "{}-squared.{}".format(os.path.splitext(filename)[0], "png")

            background.save(os.path.join(current_path, titled_thumbnail))
            background.close()
        except FileNotFoundError as err:
            print("File not found in folder")
            print(err)
        except Exception as err:
            print("An exception occurred when saving thumbnail files.")
            print(err)


@click.command()
@click.argument("photo_filename", type=click.Path(exists=True), required=True)
@click.argument("episode_number", type=click.INT, required=True)
@click.option('-c', '--accent_color', type=click.STRING, default='#47A4BF',
              help='A hexadecimal code to accent color number.(Ex: #000000)',
              show_default=True)
def thumb_maker(photo_filename, episode_number, accent_color):
    """
    Makes a Thumbnail image with counter (#EPISODE)

    PHOTO_FILENAME: The name of thumbnail file (.jpg only)\n
    EPISODE_NUMBER: The number to show ni thumbnail
    """
    try:
        accent_color = accent_color.lstrip('#')
        thumb = Image.open(photo_filename)
        # [Shadow, main color]
        color = [(0, 0, 0), tuple(int(accent_color[i:i + 2], 16) for i in (0, 2, 4))]
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


cli.add_command(square_photo_new_video)
cli.add_command(thumb_maker)

if __name__ == '__main__':
    cli()
