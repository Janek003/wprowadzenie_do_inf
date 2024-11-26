#zaczynamy od i = liczba_cyfr -1 i schodzimy w dol podajac tez reszte z dzielenia przez 10**i, cyfre wyznaczamy dostajac wartosc calkowita z dzielenia reszty (na start to liczba n' potem ostatnie 'n-1' cyfrt 'n')

n_str = input("suma cyfr n, n = ")
liczba_cyfr = len(n_str)
n = int(n_str)

def suma(i, reszta):
    if i < 0: return 0
    print(reszta // 10**i)
    return (reszta // 10**i) + suma(i - 1, reszta % 10**i)

print(f"\n{suma(liczba_cyfr-1, n)}")