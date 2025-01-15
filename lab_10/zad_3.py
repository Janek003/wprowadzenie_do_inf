n = int(input("n: "))
m = int(input("m: "))

mapa = []
for i in range(n):
    curr_row = []
    for j in range(m):
        curr_row.append( int( input( f"wartosc[{i}][{j}]: " ) ) )
    mapa.append(curr_row)


najw_wartosc = sum(mapa[0])
najw_ind = 0
for ind, row in enumerate(mapa):
    if sum(row) > najw_wartosc:
        najw_ind = ind

print(f"indeks najwiekszej sumy: {najw_ind}")