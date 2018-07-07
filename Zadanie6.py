'''
Napis program sprawdzający, czy podana przez użytkowniak liczba jest:
większa od 10
mniejsza  róna 15
podzielna przez 2 (modulo)
'''

liczba = int(input("Podaj liczbę: "))
print(f'Większa od 10: {liczba > 10}')
print(f'Mniejsza równa 15: {liczba <= 15}')
print(f'Podzielna przez 2: {liczba % 2 == 0}')

