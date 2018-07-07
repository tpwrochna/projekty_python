lista = [1, 2, 3, 4, 5, 6, 7, 'kota']
print(len(lista)) # zwraca długość listy
print(lista[0]) # zwraca 1 element listy
print(lista[-1]) # zwraca ostatni element listy
print(lista[::2]) # zwraca co 2 element z listy

lista.append('ala')
print(lista)
lista.insert(3, 'kota')
print(lista)
lista.insert(-2, 'tu byłem Tony Halik')
print(lista)
lista.insert(100, "Byłem też tu")
print(lista)
lista.remove(7)
print(lista)
print(lista.count('kota')) # zlicza koty w liscie

lista[0] = 100 # podmień element 0 na 1000
print(lista)
lista[3:7] = [] # wykasuj od 4 do 7 elementu elementy listy
print(lista)
lista[3:7] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] # podmiana elementów
print(lista)