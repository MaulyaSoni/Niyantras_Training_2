from interface import Payment
from strategies import BankTransfer , PayPal , CreditCard
from process import payment_process
from crypto_payment import Crypto

def main():

    amount = 1000
    bank_tr = BankTransfer()
    payment_process(bank_tr , amount)
   
    pp = PayPal()
    payment_process(pp , amount)
    
    card = CreditCard()
    payment_process(card , amount)
    
    # Only register a new handler 
    crp = Crypto()
    payment_process(crp , amount)


if __name__ == "__main__":
    main()