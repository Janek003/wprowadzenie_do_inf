from math import sqrt

n = int(input("koniec zakresu poszukiwania: "))

tab = [True for _ in range(n-1)] # True == pierwsza

koniec_poszukiwan = int(sqrt(n))
print(koniec_poszukiwan)

for i in range(koniec_poszukiwan):
    if tab[i] == False: continue
    
    wartosc = i + 2
    for j in range(i+1, n-1):
        if (j + 2) % wartosc == 0:
            tab[j] = False

print(tab)