from interface import Bill
from strategies import RegularCustomer ,MemberCustomer , VIPCustomer
from context import Cart
from functions import switch_customer_type , get_bill
def main():
    print("\n-------Classes Way :------")
    cart_obj = Cart(RegularCustomer(1,1000))
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")

    cart_obj.set_customer_type(MemberCustomer(1,1000))
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")

    cart_obj.set_customer_type(VIPCustomer(1,1000))
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")
    

    print("\n-------Pythonic Way-------")
    customer = switch_customer_type("regular")
    print(get_bill(3 , 1000 , customer))
    customer = switch_customer_type("member")
    print(get_bill(3 , 1000 , customer))
    customer = switch_customer_type("vip")
    print(get_bill(3 , 1000 , customer))

if __name__ == "__main__":
    main()