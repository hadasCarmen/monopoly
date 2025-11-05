from monopoly.board import *
from monopoly.player import *
from monopoly.dice import *

class Game:
    def __init__(self):
        self.player1 = Player('elazar',0,1500,[])
        self.player2 = Player('hadas',0,1500,[])
        self.board=Board()
        self.board.tile_init()

    def game(self):
        for i in range(20):
            dice_move = Dice.dice()
            if self.player1.move(dice_move, self.board)==False:
                return
            dice_move = Dice.dice()
            if  self.player2.move(dice_move, self.board)==False:
                return
        for property in self.player1.propertys:
            self.player1.money+=property["price"]

        for property in self.player2.propertys:
            self.player2.money+=property["price"]
        
        if self.player1.money>self.player2.money:
            print(f"player {self.player1.name} won")
        elif self.player1.money<self.player2.money:
            print(f"player {self.player2.name} won")
        else:
            print("tie")
    