from interface import Payment

class Crypto(Payment):
    def payment_type(self , amount):
        print(f"Payment Done by Crypto , amount : {amount}")