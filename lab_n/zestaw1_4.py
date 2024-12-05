n = int(input("n>2: "))

a = [int(input("liczba: ")) for _ in range(n)]
b = []

for i in range(len(a)-2):
    suma = sum([a[j] for j in range(i,i+3)])
    b.append(suma)

print(b.index(max(b)))