from core.strategy_interface import PaymentStrategy

class PaymentProcessor:
    def __init__(self , pay : PaymentStrategy):
        self.pay = pay

    def payment_process(self , amount : int):
        return self.pay.payment_type(amount)