
from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
      self.robot = Robot("Rumba",100)
      self.dinosaur = Dinosaur("Humphrey",25,100)

    def run_game (self):
        self.display_welcome()
        self.battle_phase()
        
    def display_welcome (self):
          print("\nWelcome to the ultimate Battle. Only one will win\n") 
           
    def battle_phase (self):
      #after testing both attacks try using a while loop to get them
      # to continue attacking until their health drops below 0
      #testing our attacks
      self.robot.attack(self.dinosaur)
      #build and test dino attack
    def display_winner (self):
        print ("n\What was Robot thinking?! Dino is the winner!\n")
        print ("n\Silly Dino thought it could best a machine?! Robot is the winner!")