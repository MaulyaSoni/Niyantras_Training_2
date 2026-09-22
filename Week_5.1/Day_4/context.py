from strategy_interface import Bill
from concrete_strategies import RegularCustomer ,MemberCustomer , VIPCustomer


class Cart:
    def __init__(self , customer_type: Bill):
        self.customer_type = customer_type
   

    #Concrete concrete_strategies 
    def set_customer_type(self , customer_type : Bill):
        self.customer_type = customer_type

    def show_customer_type(self):
        return self.customer_type

    def display_bill(self) :
        return self.customer_type.calc_discount()