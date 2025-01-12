import os
import random
import time
import copy
import msvcrt

def wylosujJablko():
    head_cords_ij = player_cords_ij[-1]
    free_space = []

    for i in range(height):
        if abs(head_cords_ij[0] - i) < 5: continue
        for j in range(width):
            if abs(head_cords_ij[1] - j) < 5: continue
            if [i, j] in player_cords_ij: continue
            if plansza[i][j] != '.': continue
            free_space.append([i, j])

    if free_space == []:
        global gra_trwa
        gra_trwa = False
        print("jablko nie moglo zostac stworzone, wygrales?")
        return

    a = random.randint( 0, len(free_space) )
    return free_space[a]
    
def wyswietlPlansze():
    view_plansza = copy.deepcopy(plansza)
    
    i, j = jablko_cords_ij
    view_plansza[i][j] = 'o'
    
    for i, j in player_cords_ij:
        view_plansza[i][j] = '*'

    for i in range(height):
        for j in range(width):
            print(view_plansza[i][j], end=" ")
        print()

def poruszWeza():
    head_i, head_j = player_cords_ij[-1]

    new_i = head_i
    new_j = head_j

    if kierunek == 'N':
        new_i = head_i - 1
    elif kierunek == 'S':
        new_i = head_i + 1
    elif kierunek == 'W':
        new_j = head_j - 1
    elif kierunek == 'E':
        new_j = head_j + 1

    player_cords_ij.append( [new_i, new_j] )
    player_cords_ij.pop(0)

def zwrocKierunek(kier):
    if msvcrt.kbhit() == True:
        klawisz = msvcrt.getwch()
        if klawisz == 'w': return 'N' 
        if klawisz == 'd': return 'E' 
        if klawisz == 's': return 'S' 
        if klawisz == 'a': return 'W'
    return kier


global gra_trwa
gra_trwa = True

#a = input("relative path do planszy: ")
a = "plansza.txt"
with open(f"{os.getcwd()}\\{a}") as f:
    plansza = [[element for element in line.split(" ")] for line in f.read().split("\n")]

width = len(plansza[0])
height = len(plansza)

player_cords_ij = [ [0, 0] ]
player_cords_ij = [ wylosujJablko() ]

#wybor pierwszego kierunku, gra nie zaczyna sie dopoki nie zostanie wybrany
wyswietlPlansze()
jablko_cords_ij = wylosujJablko()

kierunek = ''
while kierunek == '':
    kierunek = zwrocKierunek(kierunek)

while gra_trwa == True:
    kierunek = zwrocKierunek(kierunek)

    time.sleep(1.5)
    os.system("cls")
    
    jablko_cords_ij = wylosujJablko()
    wyswietlPlansze()