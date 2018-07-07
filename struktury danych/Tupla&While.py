
krotka1 = (1, 2, 3, 4, 5, 'ala', 7, 'ma', 9, 'kota')

a = 0

while a <= 9:
    print(krotka1[a])
    a += 1
print(f'elementy krotki {a}')
print(krotka1[0:2])
print(krotka1[5:7:9])
print(krotka1[::2]) # co drugi element
print(krotka1[:-1]) # wyświetl tylko bez kota
print(krotka1[1:-1] # bez krańcowy elementów)
