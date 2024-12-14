numbers = []
while True:
    num = int(input("Podaj liczbę (0 kończy wprowadzanie): "))
    if num == 0:
        break
    numbers.append(num)

if len(numbers) > 0:
    first = numbers[0]
    result = sum(n for n in numbers if n < first)
    print("Suma liczb mniejszych od pierwszej podanej liczby:", result)
else:
    print("Nie wprowadzono żadnych liczb poza zerem.")
