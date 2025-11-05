
class Player:
    def __init__(self,name,location,money,propertys):
        self.name=name
        self.location=location
        self.money=money
        self.propertys=propertys
    
    def pay(self,sum_pay):
        self.money-=sum_pay
        if sum_pay<0:
            print(f"player{self.name}lose")
            return False
        return True
    
    def get_money(self,sum_get):
        self.money+=sum_get
    
    def move(self,roll_dice,board):
        current_location=self.location+roll_dice
        if current_location>len(board.board)-1:
            current_location-=len(board.board)
            self.money+=200
        self.location=current_location
        current_tile=board.current_tile(current_location)
        return current_tile.action(self)


    def buy_property(self,name_square,price):
        self.propertys.append({"name":name_square,"price":price})  
        self.pay(price)

            

        
        

        