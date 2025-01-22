import re

my_regex = "[/+]48[ ]?([0-9]{3}[ ]?){3}"

while True:
    dane = input("numer telefonu: ")
    if re.fullmatch(my_regex, dane):
        print("poprawne")
    else: print("niepoprawna")