# kolko krzyzyk

def wyswietl(pole):
    for row in pole:
        print(" ".join(element for element in row))

def czyPoleWolne(i, j, pole):
    try:
        if pole[i][j] == '.': return True
    except: return False
    
    return False

def czyGraczWygral(pole, symbol):
    for row in pole:
        if row == [symbol for _ in range(3)]: return True
    
    for col in range(3):
        full_row = 1
        
        for row in range(3):
            if pole[row][col] == symbol: continue
            full_row = 0
            break

        if full_row == 1: return True
    
    for i in range(3):
        d1 = 1
        if pole[i][2-i] == symbol: continue
        d1 = 0
        break
    if d1 == 1: return True

    for i in range(3):
        d2 = 1
        if pole[i][i] == symbol: continue
        d2 = 0
        break
    if d2 == 1: return True

    return False

def postawSymbol(pole, i, j, symbol):
    pole[i][j] = symbol
    return pole


def glowna():
    pole = [['.' for _ in range(3)] for _ in range(3)]
    wyswietl(pole)

    symbole = ['x', 'o']
    for i in range(9):
        symbol = symbole[ i % 2 ]

        print(f"RUNDA{i}, gracz: '{symbol}'")
        wiersz = int(input("Podaj wiersz: "))
        kolumna = int(input("Podaj kolumne: "))
        
        while not czyPoleWolne(wiersz, kolumna, pole):
            print(f"Pole niedostępne, gracz: '{symbol}'")
            wiersz = int(input("Podaj wiersz: "))
            kolumna = int(input("Podaj kolumne: "))
        
        pole = postawSymbol(pole, wiersz, kolumna, symbol)
        wyswietl(pole)

        if czyGraczWygral(pole, symbol):
            print(f"wygral: '{symbol}'")
            return
        
        i += 1
    print("REMIS")
        

glowna()