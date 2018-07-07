'''
Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich liczb wprowadzonych przez użytkownika.
Daj użytkownikowi możliwość zakończenia wprowadzenia liczb odpowiednią komendą. Zadaj o obsłużenie przypadku gdy
użytkownik nie wprowadzi żadnej liczby
'''



komunikat = "Podaj kolejną liczbę lub wypisz [koniec]: "

res = input(komunikat)
min = res
max = res


while res != 'koniec':
    liczba = int(res)
    if liczba > int(max):
        max = liczba
    if liczba < int(min):
        min = liczba

    res = input(komunikat)



print(f'Największa z podanych liczb to {max}')
print((f'Najmniejsza z podanych liczb to {min}'))

