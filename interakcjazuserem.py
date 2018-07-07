imie = input("Wpisz swoje imię: ")
wiek = int(input("Podaj swój wiek: "))

if wiek >= 18:
    print("Jesteś pełnoletini, idziemy na Piwo!")
else:
    print("Sory zostajesz w domu")
print("Witaj", imie, "masz ", wiek, "lat")
input("\n\n Naciśnij Enter, aby zaknczyć program: ")
