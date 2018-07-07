'''
Zadanie 6
Napisz program zamieniający miejscami w zadanej liście liczb
# TODO: uzywaj ctrl+alt+L w celu zachowania kompatybilosci z PEP-8
W konsoli możesz sprawdzić help >>> type(x) help(x.copy)
Komentowanie bloku Ctrl +/
'''

import random

liczby = [5, 2, 1, 4, 3]
print(liczby)

index_min = None  # dla liczby najmniejszej
index_max = None  # dla liczby największej

for index in range(len(liczby)):
    if index == 0:
        index_max = index
        index_min = index
    else:
        if liczby[index] > liczby[index_max]:
            index_max = index
        if liczby[index] < liczby[index_min]:
            index_min = index

print(index_min, index_max)
# TODO: Poczytać
# Uwaga nie stosujemy nazw zmiennych takich jak słowa kluczowe w


min = liczby[index_min]
max = liczby[index_max]

liczby = index_max = min
liczby = index_min = max

print(liczby)
