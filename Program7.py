'''
Napisz program zliczający liczbę wystąpień samogłosek w podanym przez użytkownika napisie
'''

import sys


samogloski = ('a', 'e', 'i', 'o', 'u', 'y')
napis = input("Podaj dowolne słowo: ")


for litera in napis:
    if (litera in samogloski) == napis:
        print(samogloski)

