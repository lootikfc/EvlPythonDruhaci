# Okrem tkinteru potrebujeme importovat aj specialnu kniznicu pre font a kniznicu
# pre generovanie nahodnych cisiel
import tkinter
import tkinter.font
import random

# Vytvorime si plochu na kreslenie. Ziadna novinka
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()

# Vytvorime si vlastny font. Do family priradime nazov fontu, do size velkost fontu
# Dalej vieme nastavit, ci chceme aby bol bold, italics, podciarknuty alebo preciarknuty
myfont = tkinter.font.Font(family = "Helvetica", size = 30, weight = "bold")


# Podobne ako pri tvoreni inych utvarov. Do kolonky font doplnime nas font
canvas.create_text(100,100, text = "Hello World", font = myfont)

# Pre vygenerovanie nahodneho pouzijeme prikaz randrange z kniznice random
# Do zatvoriek potom zadame cislo, od ktoreho chceme zacat generovat cislo.
# Druhe cislo je cislo, od ktoreho budu vsetky tieto cisla mensie
# Interval bude teda <4,8)
canvas.create_text(300,300, text = random.randrange(4,8), font = myfont)
