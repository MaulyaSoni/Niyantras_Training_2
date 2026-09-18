from interface import Bill
from strategies import RegularCustomer ,MemberCustomer , VIPCustomer
from context import Cart

def main():
    cart_obj = Cart(RegularCustomer(1,1000))
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")

    cart_obj.set_customer_type(MemberCustomer(1,1000))
    # vip = VIPCustomer(1,1000)
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")

    cart_obj.set_customer_type(VIPCustomer(1,1000))
    print(f"Customer : {cart_obj.show_customer_type()} , Bill :{cart_obj.display_bill()}")
    
if __name__ == "__main__":
    main()