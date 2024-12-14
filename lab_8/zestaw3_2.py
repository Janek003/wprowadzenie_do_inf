try:
    base = int(input("Podaj podstawę potęgi (liczba dodatnia): "))
    exponent = int(input("Podaj wykładnik potęgi (liczba dodatnia): "))
    limit = int(input("Podaj ogranicznik (liczba dodatnia): "))

    if base <= 0 or exponent <= 0 or limit <= 0:
        raise ValueError("Podano liczbę niedodatnią!")

    # Liczenie potęgi
    power_result = base ** exponent
    if power_result > limit:
        print(f"Wynik przekracza ograniczenie ({limit}). Najbliższa wartość poniżej ograniczenia: {base**(exponent-1)}")
    else:
        print(f"Wynik: {power_result}")
except ValueError as e:
    print("Błąd:", e)
