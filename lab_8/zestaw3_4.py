n = int(input("Podaj liczbę n: "))
numbers = [float(input(f"Podaj liczbę rzeczywistą [{i+1}/{n}]: ")) for i in range(n)]

# Szukanie najdłuższego niemalejącego ciągu
max_length = 1
current_length = 1
start_index = 0
max_start_index = 0

for i in range(1, len(numbers)):
    if numbers[i] >= numbers[i-1]:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
            max_start_index = i - max_length + 1
    else:
        current_length = 1

print("Indeks początkowy najdłuższego niemalejącego ciągu:", max_start_index)
print("Długość ciągu:", max_length)