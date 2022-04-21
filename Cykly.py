import tkinter

canvas = tkinter.Canvas(height = 1000, width = 1000)
canvas.pack()

x = 10

# Pokial chceme nejaku cast kodu zopakovat n- krat, vieme ju vlozit do for cyklu.
# Pocet opakovani uvedieme do zatvorky za range.
# Tento nas kod sa zopakuje 15krat.
for i in range(15):
# Kod, ktory chceme opakovat, musime odsadit pomocou tabu
    canvas.create_rectangle(x+10,30,x+30,70, fill = "brown")
    canvas.create_oval(x,10,x+40,30, fill = "green")
    x = x + 50

y = 100

# i-cko nabera rozne hodnoty podla toho, co je v zatvorke za range.
# Ak je v nej iba jedno cislo n, tak i bude nedobudat hodnoty od 0 po n-1.

# Vypis cisla od 0 do 9.
for i in range(10):
    canvas.create_text(20,y, text = i)
    y = y + 30

y = 100

# Ak su v zatvorke 2 cisla, prve z nich je prva hodnota, ktoru nadobudne,
# druhe bude opat horna hranica.
# range(a,n) teda vypise cisla od a do n-1

# Vypis cisla od 1 do 10.
for i in range(1,11):
    canvas.create_text(50,y, text = i)
    y = y + 30

y = 100
for i in range(10):
    canvas.create_text(80,y, text = i+1)
    y = y + 30
    
y = 100

# Ak su v zatvorke 2 cisla, prve z nich je prva hodnota, ktoru nadobudne,
# druhe bude opat horna hranica, tretie velkost kroku, o ktoru sa cisla i zvacsuju.
# range(a,n,b) teda vypise cisla: a, a+b, a+b+b... n-1


# Vypis parne cisla mensie ako 10
for i in range(0,10,2):
    canvas.create_text(110,y, text = i)
    y = y + 30

y = 100
for i in range(5):
    canvas.create_text(140,y, text = i*2)
    y = y + 30

y = 100

# Vypis cisla od 50 do 40
for i in range(50,40,-1):
    canvas.create_text(170,y, text = i)
    y = y + 30


y = 100
for i in range(10):
    canvas.create_text(200,y, text = 50-i)
    y = y + 30
