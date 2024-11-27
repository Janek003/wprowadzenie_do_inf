def silnia(n):
    if n >= 1:
        return n * silnia(n-1)
    else: return 1

x = int(input('Podaj liczbe: '))
wynik = silnia(x)
print(str(x) + '!= ' + str(wynik))