'''
Napisz program, który sprawdzi pełnoletność osoby na podstawie roku jej urodzenia.
'''

import datetime

data = datetime.date.year

rok = int(input("Podaj rok urodzenia: "))


if wiek >= 18:
    print("jestś pełnoletni")
else:
    print("jestś dzieckiem!")