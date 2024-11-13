import random
losowe = []
user_input = []
ile_trafionych = 0

for i in range(6):
    curr_random = random.randint(1, 40)

    while curr_random in losowe:
        curr_random = random.randint(1, 40)
    
    losowe.append(curr_random)

    curr_given = int(input(f'liczba {i+1}: '))
    while (not curr_given in range(1, 41)) or curr_given in user_input:
        curr_given = input(f'zly zakres lub juz uzyte, ponow: ')

    user_input.append(curr_given)

for item in user_input:
    if item in losowe: ile_trafionych += 1

print(f'trafiles: {ile_trafionych}\nszczesliwe liczby: {losowe}')

if ile_trafionych == 4: print('50 zl')
if ile_trafionych == 5: print('400 zl')
if ile_trafionych == 6: print('2000 zl')