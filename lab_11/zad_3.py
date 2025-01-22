import re

my_regex_calk = "[0-9]+"
my_regex_rzecz = "[0-9]+[/.][0-9]+"

while True:
    dane = input("podaj liczbe: ")
    if re.fullmatch(my_regex_calk, dane):
        print("calkowita i rzeczywista")
    elif re.fullmatch(my_regex_rzecz, dane):
        print("rzeczywista")
    else: print("niepoprawna")