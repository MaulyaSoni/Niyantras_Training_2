from interface import Payment

class CreditCard(Payment):
    def payment_type(self , amount : int):
        print(f"Payment mode Credit Card , amount : {amount}")
    
class PayPal(Payment):
    def payment_type(self , amount : int):
        print(f"Payment mode PayPal , amount : {amount}")
    
class BankTransfer(Payment):
    def payment_type(self , amount : int):
        print(f"Payment mode Bank Transfer , amount : {amount}")