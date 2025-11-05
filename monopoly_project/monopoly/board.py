from monopoly.tile import *
from monopoly.data import *

class Board:
    def __init__(self):
        self.board = None

    def current_tile(self,location):
        return self.board[location] 
           
    def tile_init(self):
        board=[]
        for tile in tiles_data:
            match tile["type"]:
                case "property":
                    current_tile=PropertyTile(tile["name"],tile["type"],tile["price"],tile["rent"], tile["city"])
                    board.append(current_tile)
                case "bonus":
                    current_tile=BonusTile(tile["name"],tile["type"],tile["amount"])
                    board.append(current_tile)
                case "tax":
                    current_tile=TaxTile(tile["name"],tile["type"],tile["amount"])
                    board.append(current_tile)
                case "go_to_jail":
                    current_tile=GoToJailTile(tile["name"],tile["type"])
                    board.append(current_tile)
                case "jail" | "start":
                    current_tile=JailTile(tile["name"],tile["type"])
                    board.append(current_tile)
        self.board = board



    
