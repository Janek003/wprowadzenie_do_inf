wynik = 0
continue_bool = True

def calc(wynik):
    curr_action = input(
        f"\nWynik: {wynik}"
        "\n\n0 - wyjscie"
        "\n1 - dodawanie"
        "\n2 - odejmowani"
        "\n3 - mnozenie"
        "\n4 - dzielenie"
        "\n5 - potegowanie"
        "\n\nOperacja: "
    )

    if curr_action == '0':
        return False

    curr_liczba = input(
        "\nInteger: "
    )

    try: curr_liczba = int(curr_liczba)
    except:
        input('You did not put in an integer...')
        return True, wynik

    match(curr_action):
        case '1': wynik += curr_liczba
        case '2': wynik -= curr_liczba
        case '3': wynik *= curr_liczba
        case '4':
            if curr_liczba != 0:
                wynik *= 1/curr_liczba
            else:
                input("Dzielenie przez zero...")
        case '5': wynik = wynik ** curr_liczba
        case _: input("operacja musi byc integer pomiedzy 0 i 5")
    
    return True, wynik

while True:
    continue_bool, wynik = calc(wynik)

    if not continue_bool:
        print(f'Koncowy wynik {wynik}')
        break