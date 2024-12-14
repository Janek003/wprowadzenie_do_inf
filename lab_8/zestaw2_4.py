n = int(input("Podaj liczbę n: "))
numbers = []

for i in range(n):
    while True:
        num = int(input(f"Podaj liczbę całkowitą (od 1 do 100) [{i+1}/{n}]: "))
        if 1 <= num <= 100:
            numbers.append(num)
            break
        else:
            print("Podano liczbę spoza zakresu, spróbuj ponownie.")

# Sprawdzanie par
if len(numbers) != len(set(numbers)):
    print("W podanej tablicy istnieje para takich samych liczb.")
else:
    print("Nie ma par takich samych liczb.")