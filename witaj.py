'''
Zadanie 1
'''


# Pole trójkąta a * h / 0.5
a = 10
h = 5
print("Pole trójkąta = ", a * h * 0.5)


# Pole koła pi r*r
pi = 3.14
r = 7
print("Pole koła = ", pi * r ** 2)

# Pole Trapezu o h = 6.5: (a+b) * h /2
a = 3
b = 9
h = 6.5
print("Pole trapezu = ", (a + b) * h / 2)


# Objętośc kuli o promieniu 7.8:  4 *pi * r*r
r = 7.8
print("Pole kuli = ", 4/3 * pi * (7/8) ** 3) # nawias (dla 7/8) dlatego, że potęgowanie ma wyższy priorytet.

# Moje dane

wysokość = 176
wiek = 37
imie = "Tomek"

print (a)
print("a ma wartość: ", a)
print(f'a ma wartość: {a}', sep='', end='') # F-String daje możliwość odczytu zmiennej bezpośrednio ze stringa | def. separator spacja, "end" = Enter default

print("\n", imie,"masz", wiek,"lat" " i", wysokość,"centrymetrów" + " wzrostu")

# Towary

cenaCukruKg = 10.0
waga = 2.5
należność = cenaCukruKg * waga

print("Zakupiłeś: ", waga, "cukru " + "po cenie: ", cenaCukruKg, "co daje: ", należność, "PLN")

print(f'''Cena: \t{cenaCukruKg:>10.2f} PLN
Waga: \t{waga:>10.1f} KG
\nNależność: {waga:>10.1f} KG po cenie{cenaCukruKg:>10.2f} PLN ={należność:>10.2f} PLN''')

# <10 wyruwnaj do lewej o 10 znaków
# ^ wyrównaj do środka
#> wyrównaj do prawej



print(f'{"Cena: ":<3} {cenaCukruKg:>10.2f} PLN\n'
       f'{"Waga: ":<2} {waga:>10.1f} Kg\n'
       f'{"Koszt: ":<7} {cenaCukruKg * waga:>5.2f} PLN')

print(7^3)
