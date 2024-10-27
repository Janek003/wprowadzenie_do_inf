import random

score_p1 = 0
score_p2 = 0

gra_p1 = True
gra_p2 = True

aces_p1 = 0
aces_p2 = 0

points_p1 = 0
points_p2 = 0

while gra_p1 or gra_p2:

    print('\n------- PLAYER 1 -------')

    card_p1 = random.randint(2, 14)

    print(f'You picked card nr. {card_p1}')

    if card_p1 < 11: score_p1 += card_p1
    elif card_p1 == 14: score_p1 += 11
    else: score_p1 += card_p1 - 9 #this gives scores for figures without ace
    
    if card_p1 == 14:
        aces_p1 += 1

    if aces_p1 == 2:
        gra_p1 = False
        points_p1 = 0
        input('Perskie oczko!')

    elif score_p1 > 21:
        gra_p1 = False
        points_p1 = 21
        input('You went over 21. Press ENTER to end your round...')
    
    elif score_p1 == 21:
        gra_p1 = False
        points_p1 = 0
        input('You got 21! Press ENTER to end your round...')

    elif input(f'Do you want to:\n1 - get another card\n2 - end the game with score {score_p1}\n[1/2]: ') == '2':
        gra_p1 = False
        points_p1 = 21 - score_p1


    print('\n------- PLAYER 2 -------')

    card_p2 = random.randint(2, 14)

    print(f'PLAYER 2: You picked card nr. {card_p2}')

    if card_p2 < 11: score_p2 += card_p2
    elif card_p2 == 14: score_p2 += 11
    else: score_p2 += card_p2 - 9 #this gives scores for figures without ace
    
    if card_p2 == 14:
        aces_p2 += 1

    if aces_p2 == 2:
        gra_p2 = False
        points_p2 = 0
        input('PLAYER 2: Perskie oczko!')

    elif score_p2 > 21:
        gra_p2 = False
        score_p2 = 21
        input('PLAYER 2: You went over 21. Press ENTER to end your round...')
    
    elif score_p2 == 21:
        gra_p2 = False
        points_p2 = 0
        input('PLAYER 2: You got 21! Press ENTER to end your round...')

    elif input(f'PLAYER 2: Do you want to:\n1 - get another card\n2 - end the game with score {score_p2}\n') == '2':
        gra_p2 = False
        points_p2 = 21 - score_p2


if points_p1 == points_p2: print('REMIS')

if points_p1 > points_p2: print('PLAYER 2 WINS')

else: print('PLAYER 1 WINS')

input('Press ENTER to exit...')