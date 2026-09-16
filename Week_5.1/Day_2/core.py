from dataclasses import dataclass

@dataclass(frozen = True)
class Order:
    customer_name: str
    items : int 
    shipping_address : str
    delivery_notes : str
    discount : int
    gift_wrap_colour : str
    priority_flag : bool

