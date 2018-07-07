'''
Zadanie 11
Napisz program, który na podstawie gracza (x, y) na planszy w przedziale od 0 do 100 wyświetli jego przybliżone położenie
(centrum prawy górny róg, górna krawędz,....) lub informację o pozycji poza planszą. Przyjmij wartość 10 jako argines krawędzi

 np: X:95
 np: Y:95
'''

x = 95
y = 95

x = int(input("Podaj pozycję gracza 'X': "))
y = int(input("Podaj pozycję gracza 'Y': "))


if x < 10:
    if y < 10:
        print("lewy górny róg")
    elif y > 90:
        print("lewy dolny róg")
    else:
        print("lewa krawędź")
elif x > 90:
    if y < 10:
        print("prawy górny róg")
    elif y > 90:
        print("prawy dolny róg")
    else:
        print("prawa krawędź")
else:
    if y < 10:
        print("górna krawędź")
    elif y > 90:
        print("dolna krawędź")
    else:
        print("środek")
