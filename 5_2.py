n = int(input('n: '))
given_values = []

for i in range(n):
    given_values.append(int(input('val: ')))

od = int(input('od: '))
do = int(input('do: '))

for item in given_values:
    if item in range(od, do+1): print(item)

print('If nothing printed no items in range')