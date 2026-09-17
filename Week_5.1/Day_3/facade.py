from core import ShippingService
from third_party_function import AdvancedShipping
from decorators import logging

class ShippingFacade:
    def __init__(self, service : ShippingService , adv : AdvancedShipping):
        self.service = service
        self.adv = adv

    @logging
    def final(self, car_cost : float, tax: int) -> dict:
        print("\n...Facade Orchaestration...")
         
        cost_with_tax = self.adv.cost_after_tax(car_cost , tax)
        final_cost = self.service.get_rate(car_cost , tax)
        
        result = {
            "cost_of_car": car_cost,
            "tax": tax,
            "cost_of_car_after_tax":cost_with_tax,
            "cost_with_insurance": final_cost
        }

        return result