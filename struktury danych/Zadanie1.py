'''
W sesji interaktywnego środowiska konsoli stwórz tuplę zawierającą 10 różnych liczb całkowitych.
Korzystając z operatora dostęu oraz wycinania pobierz:
drugi element
przedostatni element
element od trzeciego do siódmego
co trzeci element
co drugi element od konca
'''

# KROTEI NIE MOZNA EDYTOWAC JEJ WCZESNIEJ ZDEFINIOWANYCH ELEMENTOW
krotka = (1,2,3,4,5,6,7,8,9,10)

print(krotka[1]) # drugi element
print(krotka[-2]) # przedostatni element
print(krotka[2:7]) # od 3 do 7
print(krotka[::3]) # co 3 element
print(krotka[::-2]) # co drugi do końca
print(krotka[-2::-2]) # co drugi element od końca startując od przedostatniego elementu
print(krotka + ('to', 'jest', 'nowa', 'krotka'))

