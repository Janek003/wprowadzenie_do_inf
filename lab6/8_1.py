global ilosc_permutacji
ilosc_permutacji = 0

string = input("Lancuch znakow: ") #[abcsde]
string_list = [i for i in string]
string_unikalne = list(set(string_list))
string_element_list = []

for i in string_list:
    if i not in string_element_list: string_element_list.append(i)

template_curr_list = ['' for _ in range(len(string_unikalne))]
curr_str = template_curr_list


def permutuj(n, curr_str):
    if n >= len(string_unikalne):
        print(curr_str)

        global ilosc_permutacji
        ilosc_permutacji += 1

        return
    
    for i in string_unikalne:
        #print(f'\ncurr_str: {curr_str}\nn: {n}\ni: {i}, w stringu curr: {curr_str.count(i)}\ni: {i}, w stringu orginalnym: {ile_elementow}')
        if not i in curr_str:
            #print(f'\nprzypisujemy {i} do pozycji {n}')
            curr_str[n] = i
            permutuj(n+1, curr_str)
    
    curr_str[n] = ''

permutuj(0, curr_str)
print(ilosc_permutacji)