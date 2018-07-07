'''
Napisz program wyliczajacy kwotę
'''

import string
import sys


produkty = {'ziemniaki': 1.50, 'marchew': 2.0,  'kapusta': 5.50, 'ogorki': 3.20} # Produkt i jego cena

print(f'\n\t\t\t\t\t\tProdukty dostępne w Naszym sklepie: {produkty}\n')


for k, v in produkty.items():
    #print(f'{k} w cenie: {v}')


    produkt = input("\n\t\t\tzachęcamy do zakópów: Co podać? [Wpisz: 'q' jeśli chcesz wyjść ze sklepu]:   ")

    if produkt in produkty.keys() and produkt != 'q':
        #print("Co podać?")
        ile = float(input(f'Ile kg? {produkt} '))
        cena_za_zakup = ile * produkty[produkt]
        kont_zakupy = input("Czy kupujesz coś jescze [T]ak / [N]ie ? ")
        while kont_zakupy == 'T' or kont_zakupy.upper() == 't':
        #if kont_zakupy == 'T' or kont_zakupy.upper() == 't':
            produkt = input("Co jeszcze chciałbyś kupić? ")
            ile = float(input(f'Ile kg? {produkt} '))
            cena_za_zakup = ile * produkty[produkt]
        else:
            print("Do zobaczenia :)!!!")


    elif produkt not in produkty.keys() and produkt != 'q':
        print("Niestety nie mam takiego produktu!")
    elif produkt == 'q':
        print("Do zobaczenia")
        sys.exit()


ile = float(input(f'Ile kg {produkty}'))
cena_za_zakup = ile * produkty[produkt]

print(f'Poproszę o {cena_za_zakup} PLN')



