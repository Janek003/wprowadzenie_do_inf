n = int(input('n: '))
sum = 0

for i in range(n):
    current_num = int(input('number [10-50] to be squared: '))
    while current_num > 50 or current_num < 10:
        current_num = int(input('not in range[10-50], try again: '))
    current_square = current_num**2
    sum += current_square

print(sum)
