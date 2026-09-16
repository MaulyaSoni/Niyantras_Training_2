from core import Order
from builder import OrderBuilder

def main():

    # with the dataclass and method approach
    order_obj_1 = Order(
        customer_name = "MS",
        items = 2 ,
        shipping_address = "312 , Alakhnanda Complex , MujMahuda , Vadodara",
        gift_wrap_colour = "Blue",
        discount = 10,
        delivery_notes =  "Have a good day",
        priority_flag =  False,
    )
    order_obj_2 = Order(
        customer_name = "Siri",
        items = 3,
        shipping_address = "MSU , Vadodara",
        gift_wrap_colour = "Pink",
        discount = 15,
        delivery_notes =  "Wish you a very happy birthday",
        priority_flag =  False,
    )
    print("\nBy Dataclass method :-\n")
    print("\nOrder_1 :-",order_obj_1)
    print("\nOrder_2 :-",order_obj_2)

    # the builder class approach
    builder = OrderBuilder(customer_name="Siri")
    order_1 = (
        builder
        .add_order(items = 2, shipping_address = "312 , Alakhnanda Complex , MujMahuda" , delivery_notes="Have a good day") 
        .add_discount(discount = 10)
        .add_priority(True)
        .add_gift_wrap("Red")
        .build()
    )

    order_2 = (
        builder
        .add_order(items = 3, shipping_address = "MSU , Vadodara", delivery_notes = "Wish you a very happy birthday")
        .add_priority(True)
        .add_gift_wrap("Red")
        .build()
    )

    print("\nBy Builder method :-\n")
    print("\nOrder_1 :-",order_1)
    print("\nOrder_2 :-",order_2)                                      


if __name__ == "__main__":
    main()
