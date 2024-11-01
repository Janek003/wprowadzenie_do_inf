from random import *

losowa = randint(1, 10)
gratrwa = True

while gratrwa:
    podana = int(input('Zgadnij liczbe od 1 do 10: '))

    if podana == losowa:
        print('wygrales')
        gratrwa = False

    elif podana < losowa:
        print('podana liczba jest za mala')
    else:
        print('podana liczba jest za duza')

input("Nacisnij dowolny klawisz aby wyjsc...")