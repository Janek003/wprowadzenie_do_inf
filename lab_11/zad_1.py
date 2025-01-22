import re
dane = input("imie (drugie imie) nazwisko: ")
my_regex = "[A-Z][a-z]+ ([A-Z][a-z]*)*[ ]?[A-Z][a-z]+"

if re.fullmatch(my_regex, dane):
    print("poprawne")
else: print("niepoprawne")