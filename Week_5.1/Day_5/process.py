from interface import Payment
from strategies import CreditCard , PayPal , BankTransfer


def payment_process(pay :Payment , amount : int ):
    pay.payment_type(amount)