n = int(input('n >= 4: '))
while n < 4:
    n = int(input('bad value, n: '))

given_values = []
list_b = []
list_c = []

for i in range(n):
    given_values.append(int(input('val: ')))

for i in range(2, n):
    sum  = given_values[i-2] + given_values[i-1] + given_values[i]
    print(f'suma: {sum}, index: {i}')
    list_b.append([sum, i])

list_b.sort(reverse=True)

print(list_b[0], list_b[1])