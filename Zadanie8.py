'''
Napisz program, który na podstawie wprowadzonych wymiarów opakowanie, obliczy jego objętość oraz sprawdzi, czy jest ona
większa od 1 litra 1c3


a = int(input("Podaj szerokość: "))
b = int(input("Podaj wysokość: "))
c = int(input("Podaj długość: "))

print(f'Bryła o wymiarach {a}x{b}x{c} mieści 1 litr: {a * b * c >=  1000}')