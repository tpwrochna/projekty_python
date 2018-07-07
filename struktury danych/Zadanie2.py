'''
Napisz program obliczający średnią wartość z podanych przez użytkownika licz. Do przechowywania liczb, użyj listy.
Pozwól na wprowadzenie max 10 licz. Skorzystaj z funkcji wbudowanej sum().
'''

lista = []

a = 1
liczba = 0
while a < 10:
    liczba = int(input("Podaj dowolną liczbę"))
    a += 1
    lista.append(liczba)
print(f'Twoja lista wygląda tak: {lista}')

print(f'Wyliczona średnia twojej listy to {sum(lista) / len(lista)}')





#print(sum(lista))