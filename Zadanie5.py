'''
Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej przez użytkownika liczby kilometrów
,ceny paliwa oraz spalania. Zapytaj usera takze o nazwy miejscowosci.
'''

source = input("Podaj miejsce startu: ")
destination = input("Podaj miejsce docelowe: ")
#distance = int(input("Podaj dystans: "))
distance = int(input(f'Dystans pomiędzy {source} - {destination}: '))
gaz = float(input("Podaj aktualną cenę paliwa: "))
spalanie = float(input("Podaj średnie spalanie twojego auta: "))
kosztPrzejazdu = gaz * distance * spalanie / 100

print("Za przejechane ",distance, " zapłacisz ", kosztPrzejazdu, "PLN")