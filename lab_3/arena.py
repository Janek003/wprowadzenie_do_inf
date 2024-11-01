class Protagonist:
    def __init__(self, max_hp, zloto, poziom, exp, napoje, dmg):
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
            print("You don't have any potions left...")
            return
        
        if self.akt_hp != self.max_hp: self.napoje += -1
        else:
            print("You already have full hp...")
            return
        
        self.akt_hp + healing_power
        if self.akt_hp > self.max_hp: self.akt_hp = self.max_hp
        print(f'healed to {self.akt_hp} hp')

class Enemy:
    def __init__(self, name, max_hp, dmg):
        self.name = name
        self.akt_hp = max_hp
        self.max_hp = max_hp
        self.dmg = dmg

def init_protagonist():
    starting_max_hp = 100
    starting_gold = 1000
    starting_napoje = 2
    starting_dmg = 25

    gladiator = Protagonist(starting_max_hp, starting_gold,
                            1, 0, starting_napoje, starting_dmg)
    return gladiator

def goto_tavern(gladiator):
    if gladiator.akt_hp == gladiator.max_hp: 
        input("You already have full hp...")
        return

    if gladiator.zloto >= 5:
        gladiator.akt_hp = gladiator.max_hp
        gladiator.zloto += -5
        input('You are healed...')
        return

    input("You don't have enough gold...")

def goto_market(gladiator):
    potion_cost = 5
    sward_upgrade_cost = 20
    choose = input("\nWelcome to the MARKET:"
                   f"\n1 - Upgrade your sward for {sward_upgrade_cost} gold."
                   f"\n2 - Buy a potion for {potion_cost} gold."
                   "\n3 - Exit the MARKET."
                   "\n\nYour choice: ")
    match choose:
        case '1':
            if gladiator.zloto >= sward_upgrade_cost:
                gladiator.dmg += 25
                gladiator.zloto += -sward_upgrade_cost
                input(f"Your sward now deals {gladiator.dmg} damage "
                      f"and you have {gladiator.zloto} gold...")
            else: input("You don't have enough gold...")
            return True

        case '2':
            how_many_potions = int(input('How many potions do you want to buy: '))
            if gladiator.zloto >= how_many_potions*potion_cost:
                gladiator.napoje += how_many_potions
                gladiator.zloto += -how_many_potions*potion_cost
                input(f"You now have {gladiator.napoje} health potions " 
                      f"and {gladiator.zloto} gold...")
            else: input("You don't have enough gold...")
            return True

        case '3':
            return False


def petla_glowna(gladiator):

    print(f"\nakt_hp = {gladiator.akt_hp}"
          f"\nmax_hp = {gladiator.max_hp}"
          f"\nzloto = {gladiator.zloto}"
          f"\npoziom = {gladiator.poziom}"
          f"\nexp = {gladiator.exp}"
          f"\nnapoje = {gladiator.napoje}"
          f"\ndmg = {gladiator.dmg}")

    choice = input("\nWhat do you want to do?"
                   "\n1 - Sleep in a tavern."
                   "\n2 - Go to local market."
                   "\n3 - Fight a simple enemy."
                   "\n4 - Fight a tough enemy."
                   "\n5 - Fight the final boss."
                   "\n6 - Give up."
                   "\n\nYour choice: ")
    match choice:
        case '1':
            goto_tavern(gladiator)
            return True
        
        case '2':
            while True: 
                if not goto_market(gladiator): break
            return True
        
        case '3':
            return True
        
        case '4':
            return True
        
        case '5':
            return True
        
        case '6':
            input('You have chosen to give up...')
            return False
        
        case _: input('Invalid anwser, input an int between 1 and 6')
    

def main():
    gladiator = init_protagonist()

    while True:
        if not petla_glowna(gladiator): break
        

if __name__ == "__main__":
    main()