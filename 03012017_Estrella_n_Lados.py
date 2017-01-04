#ESCUELA POLITECNICA NACIONAL
#ESCUELA DE FORMACION DE TECNOLOGOS 
#NOMBRE: DAVID CHULDE
#FECHA:03/01/2017
#PROGRAMA GENERA UNA ESTRELLA INGRESANDO EL NUMERO DE LADOS DE LA MISMA 

import turtle
a=int(input('Igrese el numero de lados de la estrella: '))
t=turtle.Pen()
t.reset()
#creacion de la estrella con un numero par
m=180+(180/a)
c=(a-2)*(180/a)
if a%2==0:
    for x in range (a):
        t.left(c)
        t.forward(100)

#creacion de la estrella con un numero impar
else:
    for x in range (a):
        t.forward(100)
        t.left(m)

turtle.getscreen()._root.mainloop()
