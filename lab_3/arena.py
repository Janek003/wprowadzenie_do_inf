import random

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
            input("You don't have any potions left...")
            return
        
        if self.akt_hp != self.max_hp: self.napoje += -1
        else:
            input("You already have full hp...")
            return
        
        self.akt_hp += healing_power
        if self.akt_hp > self.max_hp: self.akt_hp = self.max_hp
        input(f'healed to {self.akt_hp} hp...')

class Enemy:
    def __init__(self, max_hp, dmg, gold_reward, exp_reward):
        self.akt_hp = max_hp
        self.max_hp = max_hp
        self.dmg = dmg
        self.gold_reward = gold_reward
        self.exp_reward = exp_reward

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
                   f"\n1 - Upgrade your sward ({sward_upgrade_cost} gold)."
                   f"\n2 - Buy a potion ({potion_cost} gold)."
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

def fight(gladiator, type):
    if type == 'simple':
        hp_random = random.randint(40, 60)
        dmg_random = random.randint(10, 20)
        gold_reward = random.randint(10, 15)
        exp_reward = random.randint(30, 40)

    if type == 'tough':
        hp_random = random.randint(90, 110)
        dmg_random = random.randint(40, 60)
        gold_reward = random.randint(25, 35)
        exp_reward = random.randint(50, 70)

    if type == 'final_boss':
        hp_random = 550
        dmg_random = 100
        gold_reward = random.randint(50, 60)
        exp_reward = random.randint(100, 125)

    oponent = Enemy(hp_random, dmg_random, gold_reward, exp_reward)

    fight_on = True

    while fight_on:
        if gladiator.akt_hp <= 0:
            fight_on = False
            gladiator.zloto = 0
            gladiator.napoje = 0
            gladiator.akt_hp = 75
            input('\nYou died, lost all your gold and potions...')
            return False
        
        if oponent.akt_hp <= 0:
            input(f'\nYou defeated your opponent\nYou get: {oponent.gold_reward} gold and {oponent.exp_reward} exp.')
            gladiator.exp += oponent.exp_reward
            gladiator.zloto += oponent.gold_reward
            fight_on = False
            del oponent
            return True

        will_miss = random.randint(1,4)//4
        print(f"\nYour stats. HP:{gladiator.akt_hp} / {gladiator.max_hp} \tDMG: {gladiator.dmg}")
        print(f"Oponents stats. HP: {oponent.akt_hp} / {oponent.max_hp} \tDMG: {oponent.dmg}")
        choice = input(f"\nYour turn.\n1 - Attack."
                       f"\n2 - Heal ({gladiator.napoje} potions left.)"
                       f"\n3 - Run away."
                       f"\nYour choice: ")
        
        if choice == '1':
            if will_miss != 1:
                input(f'You took {gladiator.dmg} hp from your oponent...')
                oponent.akt_hp += -gladiator.dmg
            else: input('\nYou missed your attack...')
        

        if choice == '3':
            input('\nYou chose to run away...')
            fight_on = False
            break

        if choice == '2':
            gladiator.heal()
        
        else:
        #enemys turn if im not healing
            will_miss = random.randint(1,4)//4
            if will_miss != 1:
                input(f'Your opponent hit you with {oponent.dmg} dmg...')
                gladiator.akt_hp += - oponent.dmg
            else: input('Your opponent missed...')



def petla_glowna(gladiator):
    gladiator.poziom = (gladiator.exp // 100) + 1
    
    if gladiator.akt_hp == gladiator.max_hp:
        gladiator.max_hp = 100 + (50 * (gladiator.poziom-1))
        gladiator.akt_hp = gladiator.max_hp
    else: gladiator.max_hp = 100 + (50 * (gladiator.poziom-1))

    print(f"\nakt_hp = {gladiator.akt_hp}"
          f"\nmax_hp = {gladiator.max_hp}"
          f"\nzloto = {gladiator.zloto}"
          f"\npoziom = {gladiator.poziom}"
          f"\nexp = {gladiator.exp%100} / 100"
          f"\nnapoje = {gladiator.napoje}"
          f"\ndmg = {gladiator.dmg}")

    choice = input("\nWhat do you want to do?"
                   "\n1 - Sleep in a tavern (5 gold)."
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
            fight(gladiator, 'simple')
            return True
        
        case '4':
            fight(gladiator, 'tough')
            return True
        
        case '5':
            if gladiator.poziom >= 3:
                if fight(gladiator, 'final_boss'):
                    input('You won the game, congrats!')
                    return False
                    
            else: input('You have to be a level 3 gladiator to fight the final boss...')
            return True
        
        case '6':
            input('You have chosen to give up...')
            return False
        
        case _: 
            input('Invalid anwser, input an int between 1 and 6...')
            return True
    

def main():
    gladiator = init_protagonist()

    while True:
        if not petla_glowna(gladiator): break
        

if __name__ == "__main__":
    main()