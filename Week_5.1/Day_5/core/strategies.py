from core.strategy_interface import PaymentStrategy

class CreditCard(PaymentStrategy):
    def payment_type(self , amount : int):
        print(f"Payment mode Credit Card , amount : {amount}")
    
class PayPal(PaymentStrategy):
    def payment_type(self , amount : int):
        print(f"Payment mode PayPal , amount : {amount}")
    
class BankTransfer(PaymentStrategy):
    def payment_type(self , amount : int):
        print(f"Payment mode Bank Transfer , amount : {amount}")