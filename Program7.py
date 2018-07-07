'''
Napisz program zliczający liczbę wystąpień samogłosek w podanym przez użytkownika napisie
'''

import sys


SAMOGLOSKI = "aeiouy" # Duzymi bo deklarujemy stale
text = input("Podaj dowolnz napis: ")
ile_samoglosek = 0

for znak in text:
    if znak.lower() in SAMOGLOSKI:
        ile_samoglosek += 1

        for znak in text:
    if znak.lower() in SAMOGLOSKI:
        ile_samoglosek += 1


for s in SAMOGLOSKI:
    ile_samoglosek += text.lower().count(s)

print(f'Znaleziono {ile_samoglosek} samogłoske')




