def zamien(tablica, indeks1, indeks2):
    a = tablica[indeks1]
    tablica[indeks1] = tablica[indeks2]
    tablica[indeks2] = a
    
    return tablica

def bubble_sort(tab):
    for zasieg in range(len(tab) - 1, 0, -1):
        for i in range(zasieg):
            if tab[i] > tab[i + 1]:
                tab = zamien(tab, i, i+1)
    return tab

nazwa_plik = input("nazwa pliku z danymi: ")
adres_plik = f"swieta\\{nazwa_plik}.txt"
with open(adres_plik, 'r') as f:
    vals = [int(i) for i in f.read().split()]
    print(vals)

vals = bubble_sort(vals)
with open("swieta\\wynik.txt", 'w') as f:
    for item in vals:
        f.write(f"{item}\n")