from interface import ShippingService
from third_party_function import AdvancedShipping
from decorators import logging 
# Adapters
class ShippingAdapter(ShippingService):
    def __init__(self, sdk: AdvancedShipping):
        self.sdk = sdk

    @logging
    def get_rate(self, car_cost: float, tax: int) -> float:

        print("\n...Adapter....-> converting price of car from USD to INR\n")

        car_cost = int(car_cost * 92)

        print("Cost in INR : ",car_cost)
        
        return self.sdk.cost_after_tax(car_cost, tax)