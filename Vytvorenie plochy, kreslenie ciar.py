#Naimportujeme si kniznicu pre pracu s plochou na kreslenie
import tkinter

#Do premennej canvas si vytvorime objekt- plochu na kreslenie
canvas = tkinter.Canvas(height = 400, width = 400)
canvas.pack()

#V canvase vytvorime ciaru.
#Do zatvoriek idu suradnice zaciatocneho a koncoveho bodu
canvas.create_line(0,0,100,20)

#Ciaram vieme nastavovat doplnkove vlastnosti
#Farba (fill)
canvas.create_line(200,30,300,30,fill = "pink")
#Hrubka (width)
canvas.create_line(200,60,300,60,width = 5)
#Prerusovana ciara (dash)
canvas.create_line(200,90,300,90, dash = (4,3))
#Tieto vlastnosti vieme aj kombinovat
canvas.create_line(200,120,300,120, fill = 'pink', width = 5, dash = (7,4))
