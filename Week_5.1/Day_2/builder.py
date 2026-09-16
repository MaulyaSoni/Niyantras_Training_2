from core import Order

class OrderBuilder:
    
    def __init__(self, customer_name: str):
        self.customer_name: str = customer_name

    def add_order(self, items : int, shipping_address : str, delivery_notes : str):
        self.items =  items
        self.shipping_address = shipping_address
        self.delivery_notes = delivery_notes

        return self

    def add_discount(self , discount : int):
        self.discount = discount

        return self
    
    def add_gift_wrap(self , gift_wrap_colour : bool ):
        self.gift_wrap_colour= gift_wrap_colour

        return self 

    def add_priority(self , priority_flag : bool):
        self.priority_flag = priority_flag

        return self

    def build(self) -> Order:
        """Final gatekeeper check. Freezes and returns the immutable House."""
      
        if self.items < 1:
            raise ValueError(f"Items can't be 0 or less than it")
        if 0 > self.discount > 100:
            raise ValueError("Discount can't be have this value")
        
        details = Order(
            customer_name = self.customer_name,
            items = self.items,
            shipping_address = self.shipping_address,
            delivery_notes = self.delivery_notes,
            discount = self.discount,
            gift_wrap_colour = self.gift_wrap_colour,
            priority_flag = self.priority_flag
        )
    
        return details
