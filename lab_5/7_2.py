def get_input():
    choice  = int(input(
            "\n(1)dodaj na koniec"
            "\n(2)usun z konca"
            "\n(3)suma elementow"
            "\n(4)wyjscie"
            "\nChoice: "
            ))
    return choice

def dodaj(choice):
    if choice == 1:
        a = int(input('To append: '))
        ls.append(a)
        input(f'{ls}\n...')

def usun(choice):
    if choice == 2:
        ls.pop(len(ls) - 1)
        input(f'{ls}\n...')

def sumuj(choice):
    if choice == 3:
        input(f'{sum(ls)}\n...')

def kont(choice):
    if choice == 4: return False
    return True


ls = []

choice = 1

while kont(choice):
    choice = get_input()
    dodaj(choice)
    usun(choice)
    sumuj(choice)