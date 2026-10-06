from core.strategy_interface import PaymentStrategy
from core.strategies import BankTransfer , PayPal , CreditCard
from core.process import PaymentProcessor
from external_payments.crypto_payment import CryptoPayment
from core.factory import PaymentFactory

PaymentFactory.register("credit_card", CreditCard)
PaymentFactory.register("paypal",PayPal)
PaymentFactory.register("bank_transfer",BankTransfer)

def main():
    amount = int(input("Enter the amount you want to send :"))    
    payment_type = str(input("Enter the preferred payment_type : "))
    strategy = PaymentFactory.execute(payment_type)
    print(strategy)
    processor = PaymentProcessor(strategy)
    print(processor)
    processor.payment_process(amount)


    # payment_methods = [
    #     "credit_card","paypal","bank_transfer"
    # ]
    # for method in payment_methods:
    #     strategy = PaymentFactory.execute(method)
    
    # processor = PaymentProcessor(strategy)
    # processor.payment_process(amount)


    # bank_tr = BankTransfer()
    # payment_process(bank_tr , amount)
   
    # pp = PayPal()
    # payment_process(pp , amount)
    
    # card = CreditCard()
    # payment_process(card , amount)
    
    # # Only register a new handler 
    # crp = Crypto()
    # payment_process(crp , amount)


if __name__ == "__main__":
    main()