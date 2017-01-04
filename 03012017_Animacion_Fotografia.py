#ESCUELA POLITECNICA NACIONAL
#ESCUELA DE FORMACION DE TECNOLOGOS
#NOMBRE: DAVID CHULDE
#FECHA:03/01/2017
#PROGRAMA QUE CREA UNA ANIMACION  CON UNA FOTOGRAFIA-
#Y PERMITE QUE SEA MANEJADO POR TECLADO 

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)#ventana
canvas.pack()
my_image=PhotoImage(file="david1.gif")
canvas.create_image(0,0,anchor=NW,image=my_image)
def movepacman(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
canvas.bind_all('<KeyPress-Up>', movepacman)
canvas.bind_all('<KeyPress-Down>', movepacman)
canvas.bind_all('<KeyPress-Left>', movepacman)
canvas.bind_all('<KeyPress-Right>', movepacman)
tk.mainloop()
