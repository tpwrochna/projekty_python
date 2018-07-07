'''
Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie  pomiędzy nawiasami <>
Nawiasy mogą wystapic tylko raz
'''


napis = input("Podaj dowolny napis: ")
zlicz_znaki = 0

print(napis)

for znak in napis:
    zlicz_znaki += 1
    if zlicz_znaki == '<>':
        zlicz_znaki += 1

print(zlicz_znaki)


