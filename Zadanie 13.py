'''
Zadanie 13
Napisz program obliczający średnią wartość temperatury w danym tygodniu (7 dni) na podstawie temperatury
 podanych przez człowieka Wynik (suma) dzielimy dni
'''



a = 1
srednia = 0

while a <=7:
    dzien = int(input("Podaj temperaturę w dniu dzisiejszym: "))
    a += 1

    srednia = (dzien + dzien) / 7
print("średnia temperatura z całego tygodnia to: ",srednia)

print("wykonało się ", a, "razy")

#------------------------------------------------------------------------------

ilosc_dni = 7 # 7 dni tygodnia :)
nr_dnia = 1 # ustawienie zmiennej sterujacej
suma_temp = 0 # uwaga zbierasz więc zacznij od 0 jeśli dodajesz, a jeżeli mnożysz to zacznij od 1

while nr_dnia <= ilosc_dni: # Warunke pętli "Do póki nr_dnia jest mniejsze lub równe 7
    temp = int(input(f'Podaj temperaturę z dnia {nr_dnia}: '))
    suma_temp = temp + suma_temp
    nr_dnia =+ 1 # inkrementacja zmiennej sterującej do wykonania pętli

srednia_temp = suma_temp / ilosc_dni

print(f'średnia temaperatura w tym tygodniu wynisła: {srednia_temp}')