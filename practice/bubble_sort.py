import random

def zamien(tablica, indeks):
  a = tablica[indeks]
  tablica[indeks] = tablica[indeks + 1]
  tablica[indeks + 1] = a
  
  return tablica

def czyPosortowana(tablica):
  for i in range(len(tablica) - 1):
    if tablica[i] > tablica[i+1]: return False
  return True

def sortuj(tablica):
  for zasieg in range(len(tablica) - 1, 0, -1):
    for ptr in range(zasieg):
      if tablica[ptr] > tablica[ptr + 1]: zamien(tablica, ptr)
      if czyPosortowana(tablica): return tablica
  return tablica

def wyszukajBinarnie(posortowana_tablica, szukana):
  ptr_start = 0
  ptr_end = len(posortowana_tablica) - 1
  while ptr_start <= ptr_end:
    ptr_middle = (ptr_end + ptr_start) // 2
    curr_liczba = posortowana_tablica[ptr_middle]
    if curr_liczba == szukana: return ptr_middle
    if curr_liczba > szukana:
      ptr_end = ptr_middle - 1
    if curr_liczba < szukana:
      ptr_start = ptr_middle + 1
  print("nie znaleziono")
  return None


tab = [random.randint(0,50) for _ in range(random.randint(5, 25))]
print(tab)

tab = sortuj(tab)
print(tab)

a = int(input("szukana: "))
print( wyszukajBinarnie(tab, a) )