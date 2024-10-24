import random
pola = "01234567890123456789"
oznaczenie_pola = "00a000000b000e000c0d"

game_finished = False

pozycja_p1 = 0
pozycja_p2 = 0

while not game_finished:

    pozycja_p1 += random.randint(1, 4)

    if pozycja_p1 >= 19:

        game_finished = True

test = "01"

print(test[2])

