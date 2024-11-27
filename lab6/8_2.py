from copy import deepcopy

# n = int(input("n -> liczba dyskow, n = "))
n = 4

min_moves = sum(2**i for i in range(n))
print(min_moves)

poles_init = [[] for _ in range(3)]
for i in range(n-1, -1, -1): poles_init[0].append(i)
print(poles_init)

which_to_move = [0 for _ in range(min_moves)]
for a in range(n):
    for i in range(2**a - 1, min_moves - (2**a - 1), 2**(a+1)): which_to_move[i] = a
print(which_to_move)
print('---------------')

def smallestOnPoleNr(pole_nr, poles):
    if poles[pole_nr] == []: return n
    return min(poles[pole_nr])

def canDiscGoThereNow(move_nr, pole_nr, poles):
    disc = which_to_move[move_nr]
    if disc >= smallestOnPoleNr(pole_nr, poles): return False 
    return True

def moveDiscFromTo(disc, pole_from, pole_to, poles):
    updated_poles = deepcopy(poles)
    updated_poles[pole_from].remove(disc)
    updated_poles[pole_to].append(disc)
    return updated_poles

def whereIsDisc(disc, poles):
    for i in range(3):
        if disc in poles[i]: return i

def findMove(move_nr, poles):
    if move_nr == min_moves:
        if poles[2] == [i for i in range(n-1, -1, -1)]:
            print(f"finished: {poles}")
            return True
        else:
            return False

    disc = which_to_move[move_nr]
    curr_disc_position = whereIsDisc(disc, poles)
    if disc > smallestOnPoleNr(curr_disc_position, poles): 
        return False 

    for pole_nr in range(3):
        if canDiscGoThereNow(move_nr, pole_nr, poles):
            updated_copy_of_poles = moveDiscFromTo(disc, curr_disc_position, pole_nr, poles)
            findMove(move_nr+1, deepcopy(updated_copy_of_poles))
    return False        

findMove(0, deepcopy(poles_init))
# najwiekszym problemem bylo dodawanie ruchow do bad_moves
# nie powinno istniec cos takiego jak bad moves
# jesli jest on zly to sam algorytm wycofa sie z tej drogi zwracajac falsz dla dalszych krokow i przechodzac do nastepnej opcji w petli for
# uzywajac bad moves uniemozliwialem algorytmowi wykonanie ponownie tego samego ruchu dla kompletnie innego srodowiska
# ogolnie w rekursji nie mozna uzywac tej techniki, bo sama rekursja do tego slozy
# aviable moves nie maja myc najlepszymi ani prowadzacymi do sukcesu tylko rzeczywiscie mozliwymi
# to petla for odrzuca zle elementy, ta petla for przechodzi tylko raz, wiec zaden element nie bedzie probowany w nieskaczonosc