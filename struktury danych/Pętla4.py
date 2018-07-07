lista = [1, 2, 3, 4, 5, 6, 7, 8]

for el_lista in lista:
    print(el_lista)

krotka = ["ala", "ma", "kota", "ktory", "Ja", "denerwuje", "stale", " i stale"]

for el_kroka in krotka:
    print(el_kroka)

for nr, el_lista in enumerate(lista): # Pętla for, która zlicza elementy
    print(nr, el_lista)

for nr, el_lista in enumerate(lista, strt=1): # Pętla for, która zlicza elementy
    print(nr, el_lista)

print("++++++++++++++++ range (10) +++++++++++++++++++")
for nr el_kroka in enumerate(krotka, start=1):
    print(nr, el_kroka)


    >>> x.index?