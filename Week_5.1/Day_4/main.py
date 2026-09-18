from interface import Bill
from strategies import RegularCustomer ,MemberCustomer , VIPCustomer
from context import Cart
from functions import switch_customer_type , get_bill
from concrete_observers import EmailNotify , StatsUpdate , OrderEntry
from observer import CartObserver
def main():

    # val = int(input("Enter 0 for Classical Way and 1 for Pythonic way :"))
    # if val == 0:
    print("\n-------Classes Way (Classical) :------")
    cart_obj = Cart(RegularCustomer(1,1000))
    entry = OrderEntry()
    email = EmailNotify()
    stats = StatsUpdate()
    
    cart_obj.add_obs(entry)
    cart_obj.add_obs(email)
    print(cart_obj.add_obs(stats))
    
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")
    
    cart_obj.set_customer_type(MemberCustomer(1,1000))
    
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")

    cart_obj.set_customer_type(VIPCustomer(1,1000))
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")

      
    cart_obj.remove_obs(entry)
    cart_obj.remove_obs(email)
    cart_obj.remove_obs(stats)
    
    # elif val == 1:
    print("\n-------Pythonic Way-------")
    customer = switch_customer_type("regular")
    print(get_bill(3 , 1000 , customer))
    customer = switch_customer_type("member")
    print(get_bill(3 , 1000 , customer))
    customer = switch_customer_type("vip")
    print(get_bill(3 , 1000 , customer))

    
if __name__ == "__main__":
    main()