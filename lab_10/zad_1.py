import os

def wyswietlOceny(tablica):
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            print(tablica[i][j], end=" ")
        print("")

def dodajOcene(tablica):
    przedmiot = int(input(INPT_STR_1)) 
    
    if len(tablica[przedmiot]) >= 20:
        input("!!Za duzo ocen w tym przedmiocie (>=20)")
        return tablica
    
    ocena = int(input("ocena: "))
    if ocena not in range(2,6):
        input("!!Ocena nie jest z zakresu 2-5")
        return tablica
    
    tablica[przedmiot].append(ocena)
    return tablica

def usun_ocene(tablica):
    przedmiot = int(input(INPT_STR_1)) 
    indeks_oceny = int(input("indeks oceny usuwanej: "))

    try: tablica[przedmiot].pop(indeks_oceny)
    except: input("!!Nie ma oceny o takim indeksie")

def sredniaPrzedmiot(tablica, przedmiot):
    if len(tablica[przedmiot]) == 0:
        print(f"!!BRAK ocen z przedmiotu nr.{przedmiot}, srednia: 0.0")
        return float(0)
    suma = 0
    for ocena in tablica[przedmiot]:
        suma += ocena
    srednia = suma/len(tablica[przedmiot])
    print(f"srednia ocen z przedmiotu nr.{przedmiot}: {srednia}")
    return srednia

def sredniaWszystkiePrzedmioty(tablica):
    suma = 0
    for i in range(len(tablica)):
        suma += sredniaPrzedmiot(tablica, i)
    print(f"srednia wszystkich ocen: {suma/len(tablica)}")

def czyZaliczyl(tablica):
    for i in range(len(tablica)):
        if sredniaPrzedmiot(tablica, i) < 3: return False
    return True

def imprtPlik():
    a = input("podaj sciezke relatywna pliku tekstowego: ")
    our_path = f"{os.getcwd()}\\{a}"
    with open(our_path, 'r') as f:
        tablica = [[int(ocena) for ocena in line.split(" ")] for line in f.read().split("\n")]
    return tablica

oceny = [[] for _ in range(5)]

INPT_STR_1 = f"""0\twstep do informatyki
1\tnarzedzia informatyczne
2\tprogramowanie strukturalne
3\tmatematyka dyskretna
5\twstep do matematyki
przedmiot: """

INPT_STR_2 = f"""
0\twyjscie
1\tdodaj nowa ocene
2\twyswietl srednia z przedmiotu
3\twyswietl srednia ze wszystkich ocen
4\twyswietl oceny
5\tusun ocene
6\tsprawdzanie zaliczenia semestru
7\timport z pliku
wybor: """

while True:
    choice = int(input(INPT_STR_2))
    print()
    if choice == 0: break
    if choice == 1: oceny = dodajOcene(oceny)
    if choice == 2: 
        przedmiot = int(input(INPT_STR_1)) 
        sredniaPrzedmiot(oceny, przedmiot)
    if choice == 3: sredniaWszystkiePrzedmioty(oceny)
    if choice == 4: wyswietlOceny(oceny)
    if choice == 5: usun_ocene(oceny)
    if choice == 6: 
        if czyZaliczyl(oceny): print("semestr zaliczony")
        else: print("semestr NIE zaliczony")
    if choice == 7: oceny = imprtPlik()
