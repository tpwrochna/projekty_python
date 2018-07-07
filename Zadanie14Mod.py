'''
Zadanie 14
Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich liczb wprowadzonych przez użytkownika.
Daj użytkownikowi możliwość zakończenia wprowadzenia liczb odpowiednią komendą. Zadaj o obsłużenie przypadku gdy
użytkownik nie wprowadzi żadnej liczby
'''

komunikat = "Podaj kolejną liczbę lub wypisz [koniec]: "

res = input(komunikat)

# najpierw osłuż wyjątkowe sytuacje

if res == 'koniec': # W takich przypadkach obsłuż taki wyjątek to przyspiesza program i pożadkuje program
    exit("Nie podałeś żdnych liczb!")

liczba = int(res)

min = liczba
max = liczba

while True:
    res = input(komunikat)
    if res == 'koniec':
        break


    liczba = int(res)
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba

print(f'Największa z podanych liczb to {max}')
print((f'Najmniejsza z podanych liczb to {min}'))