from interface import Payment

class CreditCard(Payment):
    def payment_type(self , amount : int):
        print("Payment mode Credit Card")
    
class PayPal(Payment):
    def payment_type(self , amount : int):
        print("Payment mode PayPal")
    
class BankTransfer(Payment):
    def payment_type(self , amount : int):
        print("Payment mode Bank Transfer")