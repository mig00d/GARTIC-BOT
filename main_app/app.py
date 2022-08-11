import tkinter

import download_image
import transform_image

size = (0, 0)
cor_start_drawing = (0, 0)


def reset():
    entry.delete(0, 'end')
    label_issue.config(text=' ')


def get_drawing_zone():
    global size
    global cor_start_drawing
    size, cor_start_drawing = transform_image.get_drawing_zone()
    label_drawing_zone.config(text=f"taille de l'image: {size[0]}x{size[1]} \n"
                                   f"pixel de depart: x:{cor_start_drawing[0]}, y:{cor_start_drawing[1]}")


def get_data():
    url = str(entry.get())
    file_name = 'origin_image'
    file_path = 'images/'

    try:
        origin_image = download_image.download_image(url, file_name, file_path)
        transform_image.get_image(size, cor_start_drawing, origin_image)
    except ValueError:
        label_issue.config(text="L'adresse de l'image n'a pas été bien saisie")
    except OSError:
        label_issue.config(text='Image non compatible :(')


wn = tkinter.Tk()

# config fenêtre
wn.title('Gartic BOT')
wn.geometry('300x700+10+10')
wn.resizable(width=False, height=False)

# logo
wn.iconbitmap('../images/logo.ico')

# texte principal
label_title = tkinter.Label(wn, text='GARTIC BOT')
label_title.config(fg='blue', font=('Verdana', 28))
label_title.place(x=30, y=0)

# image gartic
image = tkinter.PhotoImage(file="../images/gartic.png")
tkinter.Label(wn, image=image, bd=0).place(x=40, y=50)

# texte info url
label_url = tkinter.Label(wn, text="Insérer l'adresse de l'image: ")
label_url.config(font=('Verdana', 13))
label_url.place(x=30, y=200)

# label d'aide
label_issue = tkinter.Label(wn, text=' ', foreground='red')
label_issue.config(font=('Verdana', 9))
label_issue.place(x=0, y=270)

# text box
entry = tkinter.Entry(wn, width=40)
entry.place(x=30, y=250)

# bouton reset
button_reset = tkinter.Button(wn, foreground='white', background='blue', text='RESET URL', command=reset, height=4,
                              width=25)
button_reset.place(x=50, y=300)

# bouton zone de dessin
button_drawing_zone = tkinter.Button(wn, foreground='white', background='green', text='DRAWING ZONE',
                                     command=get_drawing_zone, height=4, width=25)
button_drawing_zone.place(x=50, y=400)

# texte zone de dessin
label_drawing_zone = tkinter.Label(wn, foreground='green', font=('Verdana', 13), text='Choisir zone de dessin')
label_drawing_zone.place(x=30, y=500)

# bouton draw
button_draw = tkinter.Button(wn, foreground='white', background='red', text='DRAW !', command=get_data, height=4,
                             width=25)
button_draw.place(x=50, y=600)

wn.mainloop()
