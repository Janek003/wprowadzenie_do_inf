import re

my_regex = "[a-zA-Z0-9_/.]+@[a-z]+([\.][a-z])*[\.][a-z]+"

while True:
    dane = input("podaj email: ")
    if re.fullmatch(my_regex, dane):
        print("poprawne")
    else: print("niepoprawne")