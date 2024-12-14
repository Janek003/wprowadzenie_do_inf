n = int(input("n:"))

suma = 0
a = [int(input("cyfra: ")) for _ in range(n)]

for item in a:
    suma += pow(item, 2)

print(suma)