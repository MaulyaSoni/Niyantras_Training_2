from observer import CartObserver

class finalChecklist(CartObserver):
    def update(self , customer :  int , bill : float):
        print(f"All observer triggerd.. for {customer} : Bill - {bill}")