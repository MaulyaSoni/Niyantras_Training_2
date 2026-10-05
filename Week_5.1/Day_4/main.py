from strategy_interface import Bill
from concrete_strategies import RegularCustomer ,MemberCustomer , VIPCustomer
from context import Cart
from Pythonic_functions import switch_customer_type , get_bill
from concrete_observers import EmailNotify , StatsUpdate , OrderEntry
from observer import CartObserver
from subject_obs import SubjectLogger

def main():
    items = 1
    total = 1000
    print("\n-------Classes Way (Classical) :------")

   
    cart_obj = Cart(RegularCustomer(items,total))
    log_obj = SubjectLogger(cart_obj)
    entry = OrderEntry()
    email = EmailNotify()
    stats = StatsUpdate()
    
    log_obj.add_obs(entry)
    log_obj.add_obs(email)
    log_obj.add_obs(stats)

    print(f"\nCustomer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")
    log_obj.notify_observers()

    cart_obj.set_customer_type(MemberCustomer(13,10000))

    print(f"\nCustomer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")
    log_obj.notify_observers()
   
    cart_obj.set_customer_type(VIPCustomer(1,10000))

    print(f"\nCustomer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")
    log_obj.notify_observers()
                                                          
    print("\n-------Pythonic Way-------")
    customer = switch_customer_type("regular")
    print(get_bill(3 , 1000 , customer))
    customer = switch_customer_type("member")
    print(get_bill(3 , 1000 , customer))
    customer = switch_customer_type("vip")
    print(get_bill(3 , 10000 , customer))

    
if __name__ == "__main__":
    main()