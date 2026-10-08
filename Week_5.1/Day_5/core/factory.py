from core.strategy_interface import PaymentStrategy
class PaymentFactory:
    _types = {}
    # for storing the objects of the strategy classes 

    @classmethod
    def register(cls , payment_type : str , payment_val : str):
        cls._types[payment_type.lower()] = payment_val
    
    @classmethod
    def execute(cls , payment_type:str):
        payment_type = payment_type.lower()

        if payment_type not in cls._types:
            raise ValueError("The Payment type not found")
        return cls._types[payment_type]()
        # ()  trigger and runs the method 
        # and the execute method is returning the class reference itself from the _types dictionary 