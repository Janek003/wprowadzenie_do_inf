# ns builder download

poprawne_opcje = [0, 1, 2]

choice_player_1 = input("Gracz 1, (0 papier, 1 nożyce, 2 kamień): ")
while choice_player_1 not in poprawne_opcje:
    choice_player_1 = input("Gracz 1, bledny format, wprowadz ponownie: ")

choice_player_2 = input("Gracz 2, (0 papier, 1 nożyce, 2 kamień): ")
while choice_player_2 not in poprawne_opcje:
    choice_player_2 = input("Gracz 2, bledny format, wprowadz ponownie: ")
    
if choice_player_1 == 0 and choice_player_2:
    pass
