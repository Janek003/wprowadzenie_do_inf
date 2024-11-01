class Protagonist:
    def __init__(self, name, max_hp, zloto, poziom, exp, napoje, dmg):
        self.name = name
        self.akt_hp = max_hp #when initializing it always should be full
        self.max_hp = max_hp
        self.zloto = zloto
        self.poziom = poziom
        self.exp = exp
        self.napoje = napoje
        self.dmg = dmg
    
    def heal(self):
        healing_power = 50
        
        
        if self.napoje < 1:
            message = "You don't have any potions left..."
            return message
        
        if self.akt_hp != self.max_hp: self.napoje += -1
        else:
            message = "You already have full hp..."
            return message
        
        self.akt_hp + healing_power
        if self.akt_hp > self.max_hp: self.akt_hp = self.max_hp
        message = f'healed to {self.akt_hp} hp'
        
        return message

class Enemy:
    def __init__(self, name, max_hp, dmg):
        self.name = name
        self.akt_hp = max_hp
        self.max_hp = max_hp
        self.dmg = dmg

def init_protagonist():
    given_name = input('Jak masz na imie wojowniku?: ')
    starting_max_hp = 100
    starting_gold = 15
    starting_napoje = 2
    starting_dmg = 25

    gladiator = Protagonist(given_name, starting_max_hp, starting_gold,
                            1, 0, starting_napoje, starting_dmg)
    return gladiator