from core.strategy_interface import PaymentStrategy
from core.strategies import BankTransfer , PayPal , CreditCard
from core.process import PaymentProcessor
from external_payments.crypto_payment import CryptoPayment
from core.factory import PaymentFactory
from module import execute_strategy

PaymentFactory.register("credit_card", CreditCard)
PaymentFactory.register("paypal",PayPal)
PaymentFactory.register("bank_transfer",BankTransfer)

def main():

    amount = int(input("Enter the amount you want to send :"))    
    payment_type = str(input("Enter the preferred payment_type : "))

    execute_strategy(payment_type , amount)    
    
    # new payment type CRYPTO
     
    amount = int(input("Enter the amount you want to send :"))    
    payment_type = str(input("Enter the preferred payment_type : "))
    
    execute_strategy(payment_type , amount)
    
if __name__ == "__main__":
    main()