from strategy_interface import Bill
from concrete_strategies import RegularCustomer ,MemberCustomer , VIPCustomer

# Product
class Cart:
    def __init__(self , customer_type: Bill):
        self.customer_type = customer_type

    #Concrete strategies 
    def set_customer_type(self , customer_type : Bill):
        self.customer_type = customer_type

    def show_customer_type(self)-> str:
        return type(self.customer_type).__name__

    def display_bill(self) :
        return self.customer_type.calc_discount()

