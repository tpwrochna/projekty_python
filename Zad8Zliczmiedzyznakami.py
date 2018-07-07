
text = "Ala <ma> kota psota"

# Proste

start = text.index('<')
stop = text.index('>')

print(stop - start)

start = text.find('<')+1
stop = text.find('>')

print(stop - start)

czy_jest_miedzy_nawiasami = False
liczba_znakow_miedzy_nawiasami = 0

for znak int tex:
    if znak == '<':
        czy_jest_miedzy_znakami = True
    elif znak == '>':
        czy_jest_miedzy_nawiasami = False
    elif czy_jest_miedzy_nawiasami:
        liczba_znakow_miedzy_nawiasami += 1
