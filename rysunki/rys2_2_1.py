from random import *
from math import *

losowa = randint(1,20)
gracz1 = int(input('(gracz1) Zgadnij liczbe od 1 do 20: '))
gracz2 = int(input('(gracz2) Zgadnij liczbe od 1 do 20: '))

odleglosc1 = fabs(losowa - gracz1)
odleglosc2 = fabs(losowa - gracz2)

print('Wylosowana liczba wynosi: ' + str(losowa))

if odleglosc1 < odleglosc2:
    print('Wygral gracznr 1')
elif odleglosc1 > odleglosc2:
    print('WYgral gracz nr 2')
else:
    print('Remis')

input("Nacisnij dowolny klawisz aby wyjsc...")