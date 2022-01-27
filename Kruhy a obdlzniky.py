import tkinter

canvas = tkinter.Canvas(width = 400, height = 400)
canvas.pack()

#stvorec - obe suradnice sa zvysuju o rovnaku velkost
canvas.create_rectangle(10,10,40,40)
#obdlznik
canvas.create_rectangle(10,50,60,60)

#kruh - obe suradnice sa zvysuju o rovnaku velkost
canvas.create_oval(80,10,110,40)
#oval
canvas.create_oval(150,10,160,60)

#Aj ovalom a obdlznikom vieme nastavovat vlastnosti
#Vieme nastavit farbu vyplne
canvas.create_rectangle(10,200,60,230, fill = 'pink')
#Farbu obrysu
canvas.create_rectangle(10,250,60,280, outline = 'yellow')
#Hrubku obrysu
canvas.create_rectangle(10,300,60,330,width = 5)
#Prerusovany obrys
canvas.create_rectangle(10,350,60,380,dash= (2,2))


#Kruh je vpisany do stvorca - ukazka, ked maju rovnake suradnice
canvas.create_rectangle(200,200,300,300)
canvas.create_oval(200,200,300,300)
