from game import Game
import random

class Player:
    def __init__(self,neme:str):
        self.neme = neme
        Player.hp = 50
        Player.speed = random.randint(5,10)
        Player.power = random.randint(5,10)
        Player.rating_armor = random.randint(5,15)
        Player.profession = random.choice(["fighter","cure"])

    def speak(self):
        print(f"{self.neme}")

    @staticmethod
    def attack():
        my_dice = Game.roll_dice(20)
        Player.speed += my_dice
