

import random, sys

gracz_x = random.randrange(1, 11) # losuj pozycję gracza z zakresu 1-10
gracz_y = random.randrange(1, 11) # losuj pozycję gracza z zakresu 1-10

skarb_x = random.randrange(1, 11)
skarb_y = random.randrange(1,11)

skarb_x = 10
skarb_y = 10

if gracz_x and gracz_y == 11:
    sys.exc_info("Konic gry - strciłeś, życie!")

krok = input('''
Podaj, w którą stronę idziesz:
\n[l]ewo\t[p]rawo\t[g]óra\t[d]ół
\n
Wychodząc poza planszę giniesz = \'Koniec Gry\'''')


if (krok == 'l'):
        skok = int(input(f'Ile kroków chcesz wykonać: '))
        rand_pol_gracza = int(gracz_x) + skok
        if (rand_pol_gracza != skarb_x and skarb_y):
            print("Zimno jak cholera!!!")
        elif (rand_pol_gracza == skarb_x and skarb_y):
            print("Brawo Ty!")
        else:
            print("Szukaj dalej!")

elif (krok == 'p'):
    skok = int(input(f'Ile kroków chcesz wykonać: '))
    rand_pol_gracza = gracz_x + skok
    if (rand_pol_gracza != skarb_x and skarb_y):
        print("Cieplej")
    elif (rand_pol_gracza == skarb_x and skarb_y):
        print("Brawo Ty!")
    else:
        print("Szukaj dalej!")
    print("Ciepło!")
elif (krok == 'g'):
    rand_pol_gracza = gracz_x + skok
elif (krok == 'd'):
    rand_pol_gracza = gracz_x + skok
else:
    print("Nie wybrałeś kierunku poszukiwań skarbu!")


print(f'debug: {gracz_x}, {gracz_y}')
print(f'debug {skarb_x} , {skarb_y}')


