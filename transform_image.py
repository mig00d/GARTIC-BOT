from PIL import Image
from math import sqrt
from pynput.mouse import Listener, Button, Controller

# COULEUR GARTIC PHONE
RGB_WHITE = (255, 255, 255)
RGB_BLACK = (0, 0, 0)
RGB_DARK_BLUE = (0, 80, 205)
RGB_LIGHT_GREY = (170, 170, 170)
RGB_LIGHT_BLUE = (38, 201, 205)
RGB_DARK_RED = (153, 0, 0)
RGB_BROWN = (165, 65, 18)
RGB_LIGHT_GREEN = (17, 176, 60)
RGB_LIGHT_RED = (255, 0, 19)
RGB_ORANGE = (255, 120, 41)
RGB_DARK_ORANGE = (176, 112, 28)
RGB_PURPLE = (153, 0, 78)
RGB_DARK_BEIGE = (203, 90, 87)
RGB_YELLOW = (253, 193, 38)
RGB_PINK = (255, 0, 143)
RGB_DARK_GREEN = (11, 116, 32)
RGB_BEIGE = (254, 175, 168)

# toutes les couleurs de base dans gartic phone sont dans cette liste
ALL_COLOR_RGB = [RGB_BLACK, RGB_DARK_BLUE, RGB_LIGHT_GREY, RGB_LIGHT_BLUE, RGB_DARK_RED, RGB_BROWN,
                 RGB_ORANGE, RGB_DARK_ORANGE, RGB_PURPLE, RGB_DARK_BEIGE, RGB_YELLOW, RGB_PINK,
                 RGB_BEIGE, RGB_WHITE]


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

            if pixel == color:
                new_color = color
                break

            # calculer la distance de chaque pixel par rapport aux couleurs possibles
            current_distance = sqrt(
                (pixel[0] - color[0]) ** 2 + (pixel[1] - color[1]) ** 2 + (pixel[2] - color[2]) ** 2)

            # si la distance est la plus petite stocke la valeur dans minimal_distance et la couleur associée
            if current_distance < minimal_distance:
                minimal_distance = current_distance
                new_color = color

        new_image_rgb_values.append(new_color)

    return new_image_rgb_values


def resize_image(image: str, new_size: tuple, filename: str = 'resized_image.jpg'):
    """
    Retourne une image reformater de l'image de base téléchargée
    :param image:
    :param filename:
    :return:, filename: str = 'resized_image.jpg'
    """
    origin_image = Image.open(image)
    res_image = origin_image.resize(new_size)
    res_image.save(filename)
    return res_image


def on_click(x, y, button, pressed):
    if not pressed:
        # Stop listener
        return False


def calcul_coordinates(list_cor: list) -> tuple:
    """
    calcule la longueur et la largeur du carré selon
    :param list_cor:
    :return:
    """
    coor1 = list_cor[0]
    coor2 = list_cor[1]
    x_zone = int(sqrt((coor1[0] - coor2[0]) ** 2))
    y_zone = int(sqrt((coor1[1] - coor2[1]) ** 2))
    tuple_coor = (x_zone, y_zone)
    return tuple_coor


def get_drawing_zone() -> tuple:
    """
    Retourne la taille de l'image selon deux points cliquer sur l'écran et aussi les coordonnées ou le dessin commencera
    :return:
    """
    position_getter = 0
    drawing_zone = []
    mouse = Controller()

    print('faites deux clique pour choisir la zone sur laquelle le bot va dessiner')

    while position_getter < 2:

        with Listener(on_click=on_click) as listener:
            listener.join()

        drawing_zone.append(mouse.position)
        position_getter += 1

    draw_start_coordinates = drawing_zone[0]

    return calcul_coordinates(drawing_zone), draw_start_coordinates


def get_image(image_file: str, new_image_file: str = 'new_image.jpg'):
    """
    Recréer une image de base avec les couleurs de base de Gartic phone
    """

    # Les coordonnées sur le quelles le dessin doit commencer
    size, cor_start_drawing = get_drawing_zone()

    print(f'Zone confirmée de {size} pixels')

    resized_image = resize_image(image_file, new_size=size)

    print(f'reformate {image_file}')

    all_pixels = list(resized_image.getdata())

    print('Calcul des distances...')
    new_image = calcul_better_color(all_pixels)

    # créer la nouvelle image avec les bonnes couleurs
    resized_image.putdata(data=new_image)
    resized_image.save(new_image_file)
    print(f"changement de l'image {image_file} au fichier {new_image_file}")
    print("Programme terminer")


get_image(image_file='minecraft_image.jpg')
