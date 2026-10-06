from core.factory import PaymentFactory
from core.process import PaymentProcessor

def execute_strategy(payment_type , amount : int):
    strategy = PaymentFactory.execute(payment_type)
    processor = PaymentProcessor(strategy)
    return processor.payment_process(amount)
