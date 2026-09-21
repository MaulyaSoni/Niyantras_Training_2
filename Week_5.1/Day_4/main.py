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

    log_obj = SubjectLogger()
    cart_obj = Cart(RegularCustomer(items,total))

    entry = OrderEntry()
    email = EmailNotify()
    stats = StatsUpdate()
    
    log_obj.add_obs(entry)
    log_obj.add_obs(email)
    log_obj.add_obs(stats)
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")
    
    
    cart_obj.set_customer_type(MemberCustomer(1,1000))
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")

    cart_obj.set_customer_type(VIPCustomer(1,1000))
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")
    
    log_obj.notify_observers()

    log_obj.remove_obs(entry)
    log_obj.remove_obs(email)
    log_obj.remove_obs(stats)
     
    print("\n-------Pythonic Way-------")
    customer = switch_customer_type("regular")
    print(get_bill(3 , 1000 , customer))
    customer = switch_customer_type("member")
    print(get_bill(3 , 1000 , customer))
    customer = switch_customer_type("vip")
    print(get_bill(3 , 1000 , customer))

    
if __name__ == "__main__":
    main()