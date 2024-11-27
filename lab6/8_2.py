n = int(input("n -> liczba dyskow, n = "))

min_moves = sum(2**i for i in range(n))
print(min_moves)

bad_moves = [[] for _ in range(min_moves)]
print(bad_moves)

poles = [[] for _ in range(3)]
for i in range(n-1, -1, -1): poles[0].append(i)
print(poles)

which_to_move = [0 for _ in range(min_moves)]
for a in range(n):
    for i in range(2**a - 1, min_moves - (2**a - 1), 2**(a+1)): which_to_move[i] = a
print(which_to_move)

def smallestOnPoleNr(pole_nr):
    if poles[pole_nr] == []: return -1
    return min(poles[pole_nr])

def whereCanDiscGoNow(move_nr, current_disc_position):
    disc = which_to_move[move_nr]

    if disc > smallestOnPoleNr(current_disc_position): return -1 #it cannot move

    for pole_nr in range(3):
        if not(pole_nr in bad_moves[move_nr] and disc > smallestOnPoleNr(pole_nr)): 
            return pole_nr
    
    return -1

def moveDiscFromTo(disc, pole_from, pole_to, poles):
    updated_poles = poles
    updated_poles[pole_from].remove(disc)
    updated_poles[pole_to].append(disc)
    return updated_poles

def whereIsDisc(disc):
    for i in range(3):
        if disc in poles[i]: return i

def findMove(move_nr, poles):
    if move_nr == min_moves:
        if poles[2] == [i for i in range(n-1, -1, -1)]:
            print(f"finished: {poles}")
            return True
        else: return False

    disc = which_to_move[move_nr]
    curr_disc_position = whereIsDisc(disc)

    pole_aviable = whereCanDiscGoNow(move_nr, curr_disc_position)
    print(pole_aviable)

    if pole_aviable == -1: return False
    else:
        updated_poles = moveDiscFromTo(disc, curr_disc_position, pole_aviable, poles)
        print(updated_poles)
        if not findMove(move_nr+1, updated_poles):
            bad_moves[move_nr].append(pole_aviable)

findMove(0, poles)
# print()
# poles[0][3] = ''
# print(poles)
# print(smallestOnPoleNr(0))