import random

oznaczenie_pola = "00a000000b000e000c0d"

game_finished = False

pozycja_p1 = 0
pozycja_p2 = 0

skip = 0
trap = False

while not game_finished:
    
    if skip <= 0 and not trap:
        
        wylosowana = random.randint(1, 4)
        input('Click ENTER to roll the dice...')
        print(f'You rolled: {wylosowana}.')

        pozycja_p1 += wylosowana

        if pozycja_p1 >= 19:
            print('You reached the end, you won!')
            game_finished = True

        print(f'You ended up on field: {pozycja_p1}.')

        if oznaczenie_pola[pozycja_p1] == "a":
            print('You are standing on superfield(A) ->  You found a portal, you are teleporting 5 fields forward')
            pozycja_p1 += 5
            print(f'You ended up on field: {pozycja_p1}.')

        if oznaczenie_pola[pozycja_p1] == "b":
            skip = random.randint(1,3)
            print(f'You are standing on superfield(B) -> Your spaceship is broken, fixing it will take {skip} rounds')

        if oznaczenie_pola[pozycja_p1] == "c":
            print('You are standing on superfield(C) -> You remember you have forgotten something from base camp, you go back to start...')
            pozycja_p1 = 0

        if oznaczenie_pola[pozycja_p1] == "e":
            print('You are standing on superfield(E) -> You get cought up in a trap, to get out of it in the next round, you will have to roll 4, good luck...')
            trap = True



    elif skip > 0:
        skip += -1
        print(f'You are still fixing your spaceship, you have {skip} rounds left')
        input("Click ENTER to acknowledge...")
        


    elif trap:
        wylosowana = random.randint(1, 4)
        print('You are still in a trap, to free yourself - you must roll 4.')
        input('Click ENTER to roll the dice...')
        print(f'You rolled: {wylosowana}.')
        if wylosowana == 4:
            trap = False
            print("You escaped. You can move from next round on.")

    print()

input("Click ENTER to exit...")