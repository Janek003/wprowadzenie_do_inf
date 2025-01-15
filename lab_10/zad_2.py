import os
import random
import time
import copy
import msvcrt
import winsound
import threading

def beepNoBlock(frequency, duration):
    threading.Thread( target=winsound.Beep, args=(frequency, duration) ).start()

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

    a = random.randint( 0, len(free_space) - 1 )
    return free_space[a]
    
def wyswietlPlansze():

    print(f"ZYCIA: {zycia}\tPUNKTY: {punkty}")

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
    if len(player_cords_ij) > dlugosc_weza:
        player_cords_ij.pop(0)

def zwrocKierunek(kier):


    if msvcrt.kbhit():
        while msvcrt.kbhit():
            klawisz = msvcrt.getwch()

        if klawisz == 'w': return 'N' 
        if klawisz == 'd': return 'E' 
        if klawisz == 's': return 'S' 
        if klawisz == 'a': return 'W'
    return kier

def czyTraciZycie():
    for cord in player_cords_ij:
        if player_cords_ij.count(cord) > 1:
            os.system("cls")
            wyswietlPlansze()
            return True

    i, j = player_cords_ij[-1]
    if plansza[i][j] == '#': return True

    return False


global gra_trwa
gra_trwa = True

a = input("relative path do planszy: ")
#a = "plansza.txt"
with open(f"{os.getcwd()}\\{a}") as f:
    plansza = [[element for element in line.split(" ")] for line in f.read().split("\n")]

zycia = 3
dlugosc_weza = 1
punkty = 0

sleep_time_start = 0.5
sleep_time = sleep_time_start

width = len(plansza[0])
height = len(plansza)

player_cords_ij = [ [0, 0] ]
player_cords_ij = [ wylosujJablko() ]

#wybor pierwszego kierunku, gra nie zaczyna sie dopoki nie zostanie wybrany
jablko_cords_ij = wylosujJablko()

os.system("cls")
wyswietlPlansze()

kierunek = ''
while kierunek == '':
    kierunek = zwrocKierunek(kierunek)



while gra_trwa == True:

    kierunek = zwrocKierunek(kierunek)
    poruszWeza()

    if czyTraciZycie():
        winsound.Beep(500, 300)
        time.sleep(0.1)
        winsound.Beep(300, 400)
        zycia -= 1

        dlugosc_weza = 1
        sleep_time = sleep_time_start

        player_cords_ij = [ [0, 0] ]
        player_cords_ij = [ wylosujJablko() ]

        os.system("cls")
        wyswietlPlansze()

        if zycia == 0:
            input("\nKONIEC GRY...")
            break


        
        kierunek = ''
        while kierunek == '':
            kierunek = zwrocKierunek(kierunek)

    if player_cords_ij[-1] == jablko_cords_ij:
        sleep_time /= 1.03
        beepNoBlock(700, 200)
        dlugosc_weza += 1
        punkty += 1
        
        jablko_cords_ij = wylosujJablko()
        
    os.system("cls")
    wyswietlPlansze()

    time.sleep(sleep_time)
