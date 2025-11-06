
from game import Game
import random

class Goblin:
    def __init__(self,neme:str):
        self.neme = neme
        Goblin.hp = 20
        Goblin.type = "goblin"
        Goblin.speed = random.randint(5,10)
        Goblin.power = random.randint(5,10)
        Goblin.aemor_rating = 1
        Goblin.weapon = random.choice(["knife","sword","ax"])

    def speak(self):
        print(f"{self.type} {self.neme}")

    def attack():
        my_dice = Game.roll_dice(20)
        Goblin.speed += my_dice
        