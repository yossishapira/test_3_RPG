from core.player import Player
from core.orc import Orc
from core.goblin import Goblin
import random

class Game:
    def __init__(self):
        pass
    @staticmethod
    def start():
        show_manu = show_manu()
        if show_manu == 1:
            return "Play"
        else:
            return "exit"

    @staticmethod
    def show_manu():
        while True:
            entry_or_exit  = int(input("Press 1 to enter the game or 0 to exit the game."))
            if entry_or_exit == 1:
                return 1
            elif entry_or_exit == 0:
                return 0
            else:
                continue
        
    @staticmethod
    def create_player():
        create_player = Player()
        return create_player
    
    @staticmethod
    def choose_random_monster():
        random_monster = random.choice([Orc(),Goblin()])
        return random_monster
   
    @staticmethod
    def battle(player,monster):
        dice_player = Game.roll_dice(6)
        player.speed += dice_player
        dice_monster = Game.roll_dice(6)
        monster.speed += dice_monster
        if player.speed >= monster.speed:
           Game.attack(player,monster)

   
    @staticmethod
    def roll_dice(sides):
        return random.randint(1,sides)