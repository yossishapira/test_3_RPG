from game import Game
import random

class Orc:
    def __init__(self,neme:str):
        self.neme = neme
        Orc.hp = 50
        Orc.type = "orc"
        Orc.speed = random.randint(0,5)
        Orc.power = random.randint(10,15)
        Orc.aemor_rating = random.randint(2,8)
        Orc.weapon = random.choice(["knife","sword","ax"])

    def speak(self):
        print(f"{self.type} {self.neme}")


    def attack():
        my_dice = Game.roll_dice(20)
        Orc.speed += my_dice