import random

def get_values():
    while True:
        a = int(input('enter an int between 1 and 100, (0 to stop): '))
        while a not in range(0,101): a = int(input('wrong value, input again: '))
        if a == 0: break
        ls.append(a)

def make_random_list(n):
    for _ in range(n):
        ls.append(random.randint(1,100))

def znajdzmin(n):
    temp_ls = []

    for item in ls:
        if item >= n: temp_ls.append(item)
    
    print(temp_ls)

    return min(temp_ls)

def usun_elementy(elementy_list):
    for item in elementy_list:
        while item in ls: ls.remove(item)

def usun_min():
    ls.sort()
    
    print(f'out of a list: {ls}\n\ntwo smallest values are: {ls[0]} and {ls[1]}')
    for _ in range(2): ls.pop(0)

    print(ls)

ls = []

make_random_list(25)
print(ls)

input('\nENTER -> usun 2 wartosci minimalne...')
usun_min()

input('\nENTER -> znajdz min...')

n = int(input('wartosc ponizej ktorych ignorowane: '))
print(f'\nwartosc minimalna nie mniejsza od {n}: {znajdzmin(n)}')

input('\nENTER -> usun elementy...')
n = int(input('ile wartosci elementow do usuniecia: '))
b = []

for _ in range(n): b.append(int(input("wartosc: ")))

usun_elementy(b)
print(ls)