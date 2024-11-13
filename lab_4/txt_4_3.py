import random

n = int(input('How many pairs: '))

to_unflip = [i+1 for i in range(n)]

memo = []
for _ in range(2): memo.extend([i+1 for i in range(n)])

random.shuffle(memo)

while True:

    for i in range(2*n): print(f'{memo[i]}({i})', end=" ")

    print('\nleft to unflip: ', end="")
    for i in range(len(to_unflip)): print(to_unflip[i], end=" ")

    a_index = int(input('\na_index: '))
    b_index = int(input('b_index: '))

    a = memo[a_index]
    b = memo[b_index]

    print(f'{a} and {b}')

    if a == b:
        to_unflip.remove(a)

    if to_unflip == []:
        print('\nYou won!')
        break