import random, sys

gracz_x = random.randrange(1, 11) # losuj pozycję gracza z zakresu 1-10
gracz_y = random.randrange(1, 11) # losuj pozycję gracza z zakresu 1-10

skarb_x = random.randrange(1, 11)
skarb_y = random.randrange(1,11)

skarb_x = 10
skarb_y = 10

odl_przed = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
while True:

    print(f'twoja pozycja to {gracz_x}, {gracz_y}')

    if skarb_x == gracz_x and skarb_y == gracz_y:
        print("Brawo skarb należy do Ciebie!")
        break

    if ska

    krok = input()
    if krok == 'l':
        gracz_x -= 1
    elif krok == 'p':
        gracz_x += 1
    elif krok == 'g':
        gracz_y -= 1
    elif krok == 'd':
        gracz_y += 1
    else:
        continue

        odl_po = odl_przed

        if odl_przed > odl_po:
            print("Cipeło")
        else:
            print("Zimno")

    if skarb_x == gracz_x and skarb_y == gracz_y:
        print("Brawo Ty!")
        exit("Koniec")
    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print("Jestś trup!")
        break
    else:
        print("Koniec Gry")

# TODO coś tam do zrobienia
