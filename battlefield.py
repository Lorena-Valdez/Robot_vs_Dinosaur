
from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Richard",100)
        self.dinosaur = Dinosaur("Humphrey",25,100)
        pass

    def run_game (self):
        self.display_welcome()
        self.battle_phase()
        pass
        
    def display_welcome (self):
        print("\nWelcome to the ultimate Battle. Only one will win\n")
        pass
           
    def battle_phase (self):
        while self.robot.health > 0 and self.dinosaur.health >0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
        pass
             
    
    
      #after testing both attacks try using a while loop to get them
      # to continue attacking until their health drops below 0
      #testing our attacks
    #   # self.robot.attack(self.dinosaur)
    # self.health = health
    #   if health > 0:
    #     print ("Attack!")
    #   elif health < 0
    #     print ("Surrender!")
    #   break



      #build and test dino attack

    def display_winner (self):
        print ("\nWhat was Robot thinking?! Dino is the winner!\n")
        print ("\nSilly Dino thought it could best a machine?! Robot is the winner!")