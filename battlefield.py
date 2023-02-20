
from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Richard",100)
        self.dinosaur = Dinosaur("Humphrey",18,100)
        pass

    def run_game (self):
        self.display_welcome()
        self.battle_phase()
        pass
        
    def display_welcome (self):
        print("\nWelcome to the ultimate Battle. Only one will win\n")
        pass
           
    def battle_phase (self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
        
        if self.dinosaur.health >= 0:
            print (f"What was Robot thinking?! {self.dinosaur.name} is the winner!")
        elif self.robot.health >= 0:
            print (f"What was that dinosaur thinking?! {self.robot.name} is the winner!")
       

# # if loop robot/dino health greater than zero etc etc
#     def display_winner (self):