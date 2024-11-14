oceny = []

def czy_zaliczony(oceny):
    for item in oceny:
        if item <= 2: return False
    return True

def oblicz_srednia(oceny):
    if oceny == []: return "Wpisz min 1 ocene prze liczeniem sredniej"
    curr_sum = 0
    for item in oceny: curr_sum += item
    return curr_sum / len(oceny) 

while True:
    choice = int(input('\n(0)wyjdz\n(1)dodaj ocene\n(2)czy zaliczony\n(3)srednia\n(4)segreguj oceny\n(5)wyswietl oceny\nchoice: '))

    if choice == 1:
        curr_ocena = int(input('Ocena: '))
        if curr_ocena in range(2,6): oceny.append(curr_ocena)
        else: print('Nie w zakresie 2-5') 
        input('ENTER...')

    if choice == 2:
        print(czy_zaliczony(oceny))
        input('ENTER...')

    if choice == 3:
        print(oblicz_srednia(oceny))
        input('ENTER...')

    if choice == 4:
        curr_avg = oblicz_srednia(oceny)
        sortowane = oceny
        sortowane.append(curr_avg)
        oceny.sort()
        ind = sortowane.index(curr_avg)
        sortowane[ind] = 'srednia'
        print(oceny)
        input('ENTER...')

    if choice == 5:
        print(oceny)
        input('ENTER...')

    if choice == 0: break