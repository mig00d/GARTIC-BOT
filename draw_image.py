from pynput.mouse import Button, Controller
from PIL import Image
from time import sleep

# POSITION DES COULEURS DE GARTIC PHONE
POS_BLACK = (375, 310)
POS_DARK_BLUE = (440, 310)
POS_WHITE = (375, 350)
POS_LIGHT_GREY = (400, 350)
POS_LIGHT_BLUE = (440, 350)
POS_DARK_RED = (400, 390)
POS_BROWN = (440, 390)
POS_LIGHT_GREEN = (375, 430)
POS_LIGHT_RED = (400, 430)
POS_ORANGE = (440, 430)
POS_DARK_ORANGE = (375, 475)
POS_PURPLE = (400, 475)
POS_DARK_BEIGE = (440, 475)
POS_YELLOW = (375, 500)
POS_PINK = (400, 500)
POS_DARK_GREEN = (375, 390)
POS_BEIGE = (440, 500)

ALL_POS_COLOR = [
    POS_BLACK, POS_BEIGE, POS_PINK, POS_YELLOW, POS_DARK_BEIGE, POS_PURPLE, POS_DARK_ORANGE, POS_ORANGE,
    POS_LIGHT_RED, POS_BROWN, POS_DARK_RED, POS_LIGHT_BLUE, POS_LIGHT_GREY, POS_WHITE, POS_DARK_BLUE,
]


def draw(start_pixel: tuple, stop_pixel: tuple, drawing_zone: tuple, color_list: list, new_image: str = 'new_image.jpg'):
    new_image_pixel = Image.open(new_image)
    rgb_list = new_image_pixel.getdata()

    mouse = Controller()

    mouse.position = start_pixel
    counter = 0
    y_value = 5

    for i in range(0, len(rgb_list), 5):
        if counter > drawing_zone[0]:
            new_line = (start_pixel[0], start_pixel[1] + y_value)
            mouse.position = new_line
            counter = 0
            y_value += 5

            if new_line[1] > stop_pixel[1]:
                break
        sleep(0.01)
        mouse.click(Button.left, 1)
        mouse.move(5, 0)
        counter += 5

