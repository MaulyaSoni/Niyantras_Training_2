from observer import CartObserver

class OrderEntry(CartObserver):
    def update(self , customer : str , bill : float):
        print(f"Order Entry observer for {customer} for bill : {bill}")

class EmailNotify(CartObserver):
    def update(self , customer : str , bill : float):
        print(f"Email invoice sent for {customer} of bill :{bill}")

class StatsUpdate(CartObserver):
    def update(self , customer : str , bill : float):
        print(f"Stats Calculation for {customer} of bill : {bill}")
