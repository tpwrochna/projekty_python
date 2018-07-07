'''
Napisz program wypisujący wszystkie liczby od 0 do 100, podzielne prze 3 i 5. Wypisz takie liczby i zlicz ile ich jest
'''

lista = []
licznik = 0


for i in range(101):
    if (i % 3 == 0)  or (i % 5 == 0): # warunek podzielności przez 3 i 5
        print(i)
        licznik += 1
print(f'w zakresie od 0 do 100 jest {licznik}, liczb podzielnych przez 3 lub 5')

