# ns builder download
import math

poprawne_opcje = [0, 1, 2]

p1 = int(input("Gracz 1, (0 papier, 1 nożyce, 2 kamień): "))
while p1 not in poprawne_opcje:
    p1 = input("Gracz 1, bledny format, wprowadz ponownie: ")

p2 = int(input("Gracz 2, (0 papier, 1 nożyce, 2 kamień): "))
while p2 not in poprawne_opcje:
    p2 = input("Gracz 2, bledny format, wprowadz ponownie: ")

r = "remis"
n1 = "player 1 wins"
n2 = "player 2 wins"

if p1 == 0:
    
    if p2 == 0: 
        print(r)
    
    elif p2 == 1:
        print(n2)
    
    else:
        print(n1)

elif p1 == 1:
    
    if p2 == 0: 
        print(n1)
    
    elif p2 == 1:
        print(r)
    
    else:
        print(n2)

else:
    if p2 == 0: 
        print(n2)
    
    elif p2 == 1:
        print(n1)
    
    else:
        print(r)

