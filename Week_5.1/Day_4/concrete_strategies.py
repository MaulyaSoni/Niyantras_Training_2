from strategy_interface import Bill

class RegularCustomer(Bill):
    def __init__(self, items , total):
       super().__init__(items , total)
                      
    def calc_discount(self):
        match (self.items , self.total):
            case (_ , total) if total >= 5000 :
                disc = 18
            case (items ,total) if items > 17 or total >= 2500:
                disc = 9
            case (items , _) if items >= 10 : 
                disc = 3
            case _:
                disc = 1
        return Bill.discount(self , disc)

class MemberCustomer(Bill):
    def __init__(self, items , total):
       super().__init__(items , total)
                      
    def calc_discount(self):
        match (self.items , self.total):
            case (items , total) if total >= 5000 or items >= 30 :
                disc = 20
            case (_ , total)if total >= 2500 :
                disc = 15
            case (items , _) if  items > 10:
                disc = 8
            case _:
                disc = 3
        return Bill.discount(self , disc)

class VIPCustomer(Bill):
    def __init__(self, items , total):
       super().__init__(items , total)
                      
    def calc_discount(self):
        match (self.items , self.total):
            case (_ , total) if total >= 10000 :
                disc = 40
            case (_ , total) if total >= 5000:
                disc  = 25 
            case (_ , total) if total >= 1500 :
                disc = 15
            case _:
                disc = 8
        return Bill.discount(self , disc)