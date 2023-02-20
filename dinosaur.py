class Dinosaur:
    def __init__(self,name,attack_power,health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        pass

    def attack (self,robot):
        robot.health -= self.attack_power
        print(f'{robot.name} was attacked by {self.name} for {self.attack_power} Damage leaving {robot.name} with {robot.health} health remaining ')
        pass