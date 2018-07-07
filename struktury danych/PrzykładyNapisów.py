# tworzymy napis i przypisujemy go do zmiennej

napis = "ala ma kota"

# możemy sprawdzic jakie metody są dostępne dla tego typu:
print(dir(napis))
print(napis.capitalize())
print(napis.lower())
print(napis.center(80))
print(napis.count("a"))
print(napis.encode())
print(napis.find("ma")) # pokaż pozycję wystąpienia
print("To jest {}".format("Mój napis"))


b = "10a"
if b.isdigit():
    c = int(b)

napis = "*"
print(napis * 80)
napis = "Ala ma kota"
print(napis.split("ma"))

tekst = "To jest\nwieloninijkowy\napis"
print(tekst)
tekst = r"To jest\nwieloninijkowy\napis"
print(tekst)
