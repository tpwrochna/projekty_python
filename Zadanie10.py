'''
Napisz program, który na podstawie dwóch liczb obliczy wynik zadanej opracji + - * /
'''

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
znak= input("Wybierz działanie matematyczne: '+' '-' '*' '/' '%' '//' 'p'")

if (znak == '+'):
    print(f' Wynik dodawania to:  {liczba1} + {liczba2}')
elif (znak == '-'):
    print(f' Wynik dodawania to:  {liczba1} - {liczba2}')
elif (znak == '*'):
    print(f' Wynik dodawania to:  {liczba1} * {liczba2}')
elif (znak == '/' and liczba2 != 0 ):
    znak = input("Jakie dzielenie chcesz wykonać: \"%\", \"//\"?: ")
    if(znak == '%'):
        print(f' Wynik dzielenia modulo to:  {liczba1} % {liczba2}')
    elif (znak == '//'):
        print(f' Wynik dzielenia całkowitego to:  {liczba1} // {liczba2}')
    else:
        print("Nie wolno dzielić przez 0!")
#print(f' Wynik dodawania to:  {liczba1} / {liczba2}')
#elif (znak == '%'):
    #print(f' Wynik dodawania to:  {liczba1} % {liczba2}')
#elif (znak == '//'):
   # print(f' Wynik dodawania to:  {liczba1} // {liczba2}')
elif (znak == 'p'):
    print(f' Wynik potęgowania to:  {liczba1} ** {liczba1}')


else:
    print("Nie wybrałeś dobrego dziłąnia")