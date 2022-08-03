from PIL import Image
from math import sqrt
from pynput.mouse import Button, Controller

# COULEUR GARTIC PHONE
BLACK = (0, 0, 0)
DARK_BLUE = (0, 80, 205)
WHITE = (255, 255, 255)
LIGHT_GREY = (170, 170, 170)
LIGHT_BLUE = (38, 201, 205)
DARK_RED = (153, 0, 0)
BROWN = (165, 65, 18)
LIGHT_GREEN = (17, 176, 60)
LIGHT_RED = (255, 0, 19)
ORANGE = (255, 120, 41)
DARK_ORANGE = (176, 112, 28)
PURPLE = (153, 0, 78)
DARK_BEIGE = (203, 90, 87)
YELLOW = (253, 193, 38)
PINK = (255, 0, 143)
DARK_GREEN = (11, 116, 32)
BEIGE = (254, 175, 168)

# toutes les couleurs de base dans gartic phone sont dans cette liste
ALL_COLOR_RGB = [BLACK, DARK_BLUE, WHITE, LIGHT_GREY, LIGHT_BLUE, DARK_RED, BROWN,
                 LIGHT_RED, ORANGE, DARK_ORANGE, PURPLE, DARK_BEIGE, YELLOW, PINK, BEIGE]


def calcul_better_color(pixels_image) -> list:
    """
    À partir d'une liste de touts les codes RGB de l'image de base, va regarder de quelle couleur il est le moins le
    distant selon les codes RGB des couleurs de gartic phone. Puis retourne dans une liste les couleurs les plus proches
    pour tous les pixels de l'image de base.

    :param pixels_image:
    :return :
    """
    new_image_rgb_values = []
    new_color = 0

    for pixel in pixels_image:
        minimal_distance = 100000000000000000000
        for color in ALL_COLOR_RGB:
            # calculer la distance de chaque pixel par rapport aux couleurs possibles
            current_distance = sqrt(
                (pixel[0] - color[0]) ** 2 + (pixel[1] - color[1]) ** 2 + (pixel[2] - color[2]) ** 2)

            # si la distance est la plus petite stocke la valeur dans minimal_distance et la couleur associée
            if current_distance < minimal_distance:
                minimal_distance = current_distance
                new_color = color

        new_image_rgb_values.append(new_color)

    return new_image_rgb_values


def get_image(image_file: str, new_image_file: str = 'new_image.jpg'):
    """
    Recréer une image de base avec les couleurs de base de Gartic phone
    """
    # récupère l'image et tous les codes rgb de chaques pixels
    image = Image.open(image_file)
    all_pixels = list(image.getdata())

    print('Calcul des distance...')
    new_image = calcul_better_color(all_pixels)

    # créer la nouvelle image avec les bonnes couleurs
    image.putdata(data=new_image)
    image.save(new_image_file)
    print(f"changement de l'image {image_file} au fichier {new_image_file}")


mouse = Controller()
while True:
    print(mouse.position)


get_image(image_file='dogo.jpg', new_image_file='new_image.jpg')
