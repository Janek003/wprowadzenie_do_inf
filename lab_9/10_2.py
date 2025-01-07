# Zaprojektować diagram NS algorytmu wyszukiwania liniowego oraz binarnego, a
# następnie zaimplementować rozwiązanie powyższego zadania w języku Python.


# def binary_search(tablica, szukana):
#     curr_tab = tablica
#     found_index = None

#     while True:
#         curr_len = len(curr_tab)
#         curr_index = curr_len // 2
#         curr_value = curr_tab[curr_index]

#         if curr_value == szukana:
#             found_index = curr_index
#             break

#         if curr_len == 1:
#             break

#         if curr_value > szukana:
#             curr_tab = [curr_tab[i] for i in range(curr_index)]
       
#         if curr_value < szukana:
#             curr_tab = [curr_tab[i] for i in range(curr_index + 1, curr_len)]
    
#     return found_index
import random as rd

def binary_search_2(tablica, szukana):
    ptr_left = 0
    ptr_right = len(tablica) - 1
    porownan = 0
    while ptr_left <= ptr_right:
        porownan += 1
        ptr_mid = (ptr_left + ptr_right) // 2
        curr_val = tablica[ptr_mid]

        if curr_val == szukana: return ptr_mid
        
        if curr_val > szukana: ptr_right = ptr_mid - 1
        if curr_val < szukana: ptr_left = ptr_mid + 1
    
    return None


def liniar_search(tablica, szukana):
    found_index = None
    for i in range(len(tablica)):
        if tablica[i] == szukana:
            found_index = i
            return found_index

elementow = int(input("ile elementow: "))

ls = [rd.randint(0, 100) for _ in range(elementow)]
ls.sort()

print(ls)

szukana = int(input("szukana: "))
print(f"indeks szukanej liniowo: {liniar_search(ls, szukana)}")
print(f"indeks szukanej binarnie: {binary_search_2(ls, szukana)}")