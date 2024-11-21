ilosc_permutacji = 0

string = input("Lancuch znakow: ") #[abcsde]
string_list = [i for i in string]
string_element_list = []

for i in string_list:
    if i not in string_element_list: string_element_list.append(i)

template_curr_list = ['' for i in range(len(string))]
curr_str = template_curr_list


def permutuj(n, curr_str, ilosc_permutacji):
    #if n > (len(string) - 1):
        #print(curr_str)
        #curr_str[n] = ''
        #ilosc_permutacji += 1
        #return
    if n < len(string):
        for i in string_list:
            ile_elementow = string_list.count(i)
            print(f'\ncurr_str: {curr_str}\nn: {n}\ni: {i}, w stringu curr: {curr_str.count(i)}\ni: {i}, w stringu orginalnym: {ile_elementow}')
            if curr_str.count(i) < ile_elementow:
                print(f'\nprzypisujemy {i} do pozycji {n}')
                curr_str[n] = i
                permutuj(n+1, curr_str, ilosc_permutacji)
        
        curr_str[n] = ''

    return

print(f"{string} \n{curr_str}")
permutuj(0, curr_str, ilosc_permutacji)