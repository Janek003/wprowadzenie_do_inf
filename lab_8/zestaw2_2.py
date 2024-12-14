podstawa = int(input("podstawa: "))
wykladnik = int(input("wykladnik: "))

wynik = 1

for _ in range(wykladnik):
    wynik *= podstawa

print(wynik)