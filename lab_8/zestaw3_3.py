numbers = []

while True:
    num = int(input("Podaj liczbę (zakres 10–500): "))
    if num < 10 or num > 500:
        break
    numbers.append(num)

if len(numbers) < 2:
    print("Za mało liczb w podanym zakresie, aby znaleźć dwa najmniejsze.")
else:
    numbers.sort()
    print("Dwa najmniejsze elementy:", numbers[0], "i", numbers[1])
