from observer import CartObserver

class OrderEntry(CartObserver):
    def update(self , customer : str , bill : float):
        print(f"Order Entry observer for {self.customer} for bill : {self.bill}")

class EmailNotify(CartObserver):
    def update(self , customer : str , bill : float):
        print(f"Email invoice sent for {self.customer} of bill :{self.bill}")

class StatsUpdate(CartObserver):
    def update(self , customer : str , bill : float):
        print(f"Stats Calculation for {self.customer} of bill : {self.bill}")
