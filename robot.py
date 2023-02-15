from weapon import Weapon

class Robot:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Katana",25)

    def attack (self,dinosaur):
       dinosaur.health -= self.active_weapon.attack_power
       print(f'{dinosaur.name} was attacked by {self.name} for {self.active_weapon.attack_power} Damage leaving {dinosaur.name} with {dinosaur.health} health remaining ')