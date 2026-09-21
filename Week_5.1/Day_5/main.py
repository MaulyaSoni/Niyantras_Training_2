from interface import Payment
from strategies import BankTransfer , PayPal , CreditCard
from process import payment_process

def main():

    amount = 1000
    bank_tr = BankTransfer()
    payment_process(bank_tr , 1000)
   
    pp = PayPal()
    payment_process(pp , amount)
    
    card = CreditCard()
    payment_process(card , amount)
    
if __name__ == "__main__":
    main()