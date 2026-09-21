from strategy_interface import Bill

class RegularCustomer(Bill):
    def __init__(self, items , total):
       super().__init__(items , total)
                      
    def calc_discount(self):
        return Bill.discount(self , 5)

class MemberCustomer(Bill):
    def __init__(self, items , total):
       super().__init__(items , total)
                      
    def calc_discount(self):
        return Bill.discount(self , 10)

class VIPCustomer(Bill):
    def __init__(self, items , total):
       super().__init__(items , total)
                      
    def calc_discount(self):
        return Bill.discount(self , 15)