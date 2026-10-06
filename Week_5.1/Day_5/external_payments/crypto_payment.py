from core.strategy_interface import PaymentStrategy
from core.factory import PaymentFactory

class CryptoPayment(PaymentStrategy):
    def payment_type(self , amount):
        print(f"Payment Done by Crypto , amount : {amount}")

PaymentFactory.register("crypto" , CryptoPayment)