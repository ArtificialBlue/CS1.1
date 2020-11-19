import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        total_block =  0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def add_weapon(self, weapon):
        self.abilities.append(weapon)


    def take_damage(self, damage):
        defense = self.defend(damage)
        self.current_health -= (damage - defense)


    def is_alive(self):
        if (self.current_health <= 0):
            return False
        else:
            return True

    def fight(self, opponent):
        if (len(self.abilities) == 0 and len(opponent.abilities) == 0):
            print("Draw")
        else:
            while (self.is_alive() and opponent.is_alive()):
                opponent.take_damage(self.attack())
                if opponent.is_alive():
                    self.take_damage(opponent.attack())
                else:
                    pass
            if self.current_health <= 0:
                print(f"{opponent.name} won!")
            else:
                print(f"{self.name} won!")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
