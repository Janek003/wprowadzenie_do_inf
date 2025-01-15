def czyUnikalne():
    for row in tab:
        if row != set(row):
            return "Nie wszystkie unikalne"
    return "Wszystkie unikalne"

def czySymetryczna():
    for i in range(n):
        for j in range(n-i):
            if tab[i][i + j] != tab[i + j][i]: return "Niesymetryczna"
    return "Symetryczna"

def czyBrzegowych():
    brzegowe = 0
    niebrzegowe = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1: brzegowe += tab[i][j]
            else: niebrzegowe += tab[i][j]
    if brzegowe > niebrzegowe: return "Brzegowa suma wieksza"
    return "Brzegowa suma NIE wieksza"

def czyDwieTakieSame():
    for line in tab:
        for item in line:
            ile = 0
            for row in tab: ile += row.count(item) 
            if ile > 1: return "Powtarza sie co najmniej 1 wartosc"
    return "Nic sie nie powtarza"

tab = [ [ int( input(f"wartosc[{i}][{j}]: ") ) for j in range(5) ] for i in range(5) ]
# tab = [
#     [0, 1, 2, 3, 4],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 99, 20],
#     [25, 24, 19, 22, 21],
#     [0, 27, 33, 44, 66]
# ]
n = 5

print(czyUnikalne())
print(czySymetryczna())
print(czyBrzegowych())
print(czyDwieTakieSame())