n = int(input('n: '))
given_values = []

for i in range(n):
    given_values.append(int(input('val: ')))

given_values.sort()

print(given_values[-1], given_values[-2])