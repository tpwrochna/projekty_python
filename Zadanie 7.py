'''
Zadanie 7
Napisz program sprawdzajacy czy podana przez użytkownika liczba jest podzielna przez 2 i podzielna przez 3 i większa od 10
lub jest liczbą 7
'''

liczba = int(input("Podaj liczbę: "))

sprawdz = liczba % 2 == 0 and liczba % 3 == 0 and liczba
sprawdz = sprawdz or liczba == 7


print(f'liczba spełnia dgługi warunek: '
                    f'{liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10 or liczba == 7}')

