# ns builder download
import math

result = "remis"
while result == "remis":
    poprawne_opcje = ["0", "1", "2"]

    p1 = input("Gracz 1, (0 papier, 1 nożyce, 2 kamień): ")
    while p1 not in poprawne_opcje:
        p1 = input("Gracz 1, bledny format, wprowadz ponownie: ")

    p2 = input("Gracz 2, (0 papier, 1 nożyce, 2 kamień): ")
    while p2 not in poprawne_opcje:
        p2 = input("Gracz 2, bledny format, wprowadz ponownie: ")

    remisy = [["00", "11", "22"], "remis"]
    p1_win = [["10", "21", "02"], "wygrywa gracz 1"]
    p2_win = [["20", "01", "12"], "wygrywa gracz 2"]

    razem = [remisy, p2_win, p1_win]

    zlozone_p2_p1 = p1+p2

    for item in razem:
        if zlozone_p2_p1 in item[0]:
            result = item[1]
            print(result)

input("Nacisnij ENTER aby wyjsc...")