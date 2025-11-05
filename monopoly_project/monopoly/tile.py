from abc import ABC, abstractmethod

class Tile(ABC):
    def __init__(self,name_square:str,kind_square:str):
        self.name_square=name_square
        self.kind_square=kind_square
    
    @abstractmethod
    def action(self,player):
        pass


class PropertyTile(Tile):
    def __init__(self, name_square, kind_square,price_buy:int,price_rent:int,city,bought_or_not=False):
        super().__init__(name_square, kind_square)
        self.price_buy=price_buy
        self.price_rent=price_rent
        self.bought_or_not=bought_or_not
        self.city=city
    
    def action(self,player):
        if not self.bought_or_not:
            choose=input(f"choose yes to buy or not if you dont want buy it is cost:{self.price_buy}")
            if choose=="yes":
                self.bought_or_not=True
                return player.buy_property(self.name_square,self.price_buy) 
            else:
                return True
        else:
            for prop in player.propertys:
                if self.name_square not in prop["name"]:
                    return True
            print("you need pay rent",self.price_rent)
            return player.pay(self.price_rent)


class RailTile(PropertyTile):
    def __init__(self, name_square, kind_square, price_buy, price_rent, city, bought_or_not=False):
        super().__init__(name_square, kind_square, price_buy, price_rent, city, bought_or_not)
        pass

class BonusTile(Tile):
    def __init__(self, name_square, kind_square,sum_gift):
        super().__init__(name_square, kind_square)
        self.sum_gift=sum_gift
    def action(self, player):
        player.money+=self.sum_gift
        return True


class TaxTile(Tile):
    def __init__(self, name_square, kind_square,sum_tax):
        super().__init__(name_square, kind_square)
        self.sum_tax=sum_tax
    def action(self, player):
        return player.pay(self.sum_tax)

class JailTile(Tile):#dont do nothing
    def __init__(self, name_square, kind_square):
        super().__init__(name_square, kind_square)
        pass
    def action(self, player):
        return True

class GoToJailTile(Tile):
    def __init__(self, name_square, kind_square):
        super().__init__(name_square, kind_square)
        pass
    def action(self, player):
        player.location=20
        return True
    




