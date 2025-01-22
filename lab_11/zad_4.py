import re

my_regex = "([A-Z][a-z]+[ ]?)*[A-Z][a-z]+[ ][0-9]+[a-zA-Z]*([ ][0-9]+)?"

while True:
    dane = input("ulica/miejscowosc numer domu mieszkanie(opcjonalnie): ")
    if re.fullmatch(my_regex, dane):
        print("poprawne")
    else: print("niepoprawna")