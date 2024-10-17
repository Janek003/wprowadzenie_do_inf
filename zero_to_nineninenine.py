num = int(input("wpisz liczbe 0 do 999: "))

while not(num >= 0 and num <= 999):
    num = int(input("zla tresc, sprobuj ponownie: wpisz liczbe od 0 to 999: "))

num_with_zeros = str(num).zfill(3)

jednosci = int(num_with_zeros[2])
dziesiatki = int(num_with_zeros[1])
setki = int(num_with_zeros[0])

print(f"jednosci: {jednosci}")
print(f"dziesiatki: {dziesiatki}")
print(f"setki: {setki}")

print(f"suma cyfr: {jednosci + dziesiatki + setki}")