# Temou dnesnej hodiny budu premenne.
# Premennu si mozme predstavit ako nejake miesto v pamati,
# kde si zapamatame nejaku hodnotu alebo objekt
import tkinter
import random

# S premennou sme sa stretavali vlastne cely cas.
# 'canvas' je prvy priklad premennej, ktoru sme pouzivali
# V premennej 'canvas' mame ulozeny objekt Canvas z kniznice
# tkinter. Tento objekt ma potom funkcie, ktore nam umoznuju
# kreslit donho
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

# Niekolko jednoduchsich prikladov premennych:

# 1. Cislo - do premennej 'x' priradime hodnotu 4

x = 4
# Potom tuto hodnotu vypiseme do canvasu. Pokial chceme
# vypisat hodnotu premennej, nedavame ju do uvodzoviek
canvas.create_text(100,20, text = x)

# Ku premennej 'x' pripocitame 3 a vypiseme, malo by nam
# vyjst 7, lebo 'x' ma este stale hodnotu 4 z predchadzajucej
# casti kodu
x = x + 3
canvas.create_text(100,50, text = x)

# Do premennej 'x' ale mozeme priradit nejake cislo aj nanovo.
# Tu do nej priradime 5 a tato 5 prepise 7, ktora
# tam bola ulozena predtym

x = 5
canvas.create_text(100,80, text = x)

# 2. Text - do premennej 'x' priradime nejaky text, ten
# prepise hodnotu, ktora tam bola predtym.
# Text musime uviest v uvodzovkach

x = "ahoj"
canvas.create_text(100,110, text = x)

# 3. Pole - nemusime ist do detailov, kedze toto sa berie
# az na seminari. My to vsak vyuzijeme na to, aby sme vedeli
# vygenerovat nahodnu farbu nasich utvarov. Premennu nazveme
# 'pole' a priradime do nej viacero roznych textov - nazvov farieb.
# Ked toto pole vypiseme, vypisu sa nam vsetky tieto farby

pole = ['green', 'blue', 'red', 'black']
canvas.create_text(100,140, text = pole)

# Ak budeme chciet nahodne vybrat niektoru z tychto farieb,
# vieme to urobit nasledovne:

canvas.create_text(100, 170, text = pole[random.randrange(0,4)])

# Preco to funguje? Vygenerujeme nahodne cislo od 0 do 4
# a potom vypiseme dany prvok pola

# A tu si to vyskusame pri vykresleni nejakeho tvaru. Miesto
# priradenia tejto hodnoty do textu ju priradime ako nazov
# farby pre nas obdlznik

canvas.create_rectangle(250,250,300,300, fill = pole[random.randrange(0,4)])


# Teraz si mozeme skusit vykreslit stvorec pomocou premennych
# V premennych 'x' a 'y' si budeme pamatat suradnice laveho horneho
# rohu, v premennej strana bude dlzka strany stvorca

x = 300
y = 50
strana = 50

canvas.create_rectangle(x,y,x+strana, y+strana)

