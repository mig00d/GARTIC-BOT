from PIL import Image
from pynput.mouse import Listener, Controller
from math import sqrt

from main_app import draw_imageV2
from init_app.constants import ALL_COLOR_RGB


def calcul_better_color(pixels_image: list) -> list:
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
            current_distance = (pixel[0] - color[0]) ** 2 + (pixel[1] - color[1]) ** 2 + (pixel[2] - color[2]) ** 2

            # si la distance est la plus petite stocke la valeur dans minimal_distance et la couleur associée
            if current_distance < minimal_distance:
                minimal_distance = current_distance
                new_color = color

        new_image_rgb_values.append(new_color)

    return new_image_rgb_values


def resize_image(image: str, new_size: tuple, filename: str = 'resized_image.jpg'):
    """
    Retourne une image reformater de l'image de base téléchargée
    :param new_size:
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
    Calcule la longueur et la largeur du carré selon
    :param list_cor:
    :return:
    """
    coor1 = list_cor[0]
    coor2 = list_cor[1]
    x_zone = int(sqrt((coor1[0] - coor2[0]) ** 2))
    y_zone = int(sqrt((coor1[1] - coor2[1]) ** 2))
    tuple_coor = (x_zone, y_zone)

    top_left_corner = (min(coor1[0], coor2[0]), min(coor1[1], coor2[1]))
    return tuple_coor, top_left_corner


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
        print(f'Click: {mouse.position}')
        drawing_zone.append(mouse.position)
        position_getter += 1

    return calcul_coordinates(drawing_zone)


def get_image(size: tuple, cor_start_drawing: tuple, image_file: str, new_image_file: str = 'new_image.jpg'):
    """
    Recréer une image de base avec les couleurs de base de Gartic phone et redimensionner selon les clicks de l'utilisateur
    """

    print(cor_start_drawing)
    print(size)
    print(f'coté x du rectangle confirmé:  {size[0]}')
    print(f'coté y du rectangle confirmé:  {size[1]}')

    resized_image = resize_image(image_file, new_size=size)

    print(f'reformate {image_file}')

    all_pixels = list(resized_image.getdata())
    print('Calcul des distances...')
    new_image_list = calcul_better_color(all_pixels)
    # créer la nouvelle image avec les bonnes couleurs
    resized_image.putdata(data=new_image_list)
    resized_image.save(new_image_file)
    print(f"changement de l'image {image_file} au fichier {new_image_file}")

    draw_imageV2.draw(start_pixel=cor_start_drawing, color_list=ALL_COLOR_RGB,
                      new_image_list=new_image_list, drawing_zone=size)

    print("Programme terminer")
