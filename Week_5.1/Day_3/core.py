from abc import ABC, abstractmethod
from third_party_function import AdvancedShipping
from decorators import logging

# target , interface
class ShippingService(ABC):
    @abstractmethod
    def get_rate(self, car_cost: float, tax: int) -> float:
        pass

# Adapters
class ShippingAdapter(ShippingService):
    def __init__(self, sdk: AdvancedShipping):
        self.sdk = sdk

    @logging
    def get_rate(self, car_cost: float, tax: int) -> float:

        print("converting price of car from USD to INR")

        car_cost = int(car_cost * 92)

        print("Cost in INR : ",car_cost)
        
        # print("subject_interface transformation: Calls 'calculate_total_cost' instead of 'get_rate' ")
        return self.sdk.cost_after_tax(car_cost, tax)

class InsuranceDecorator(ShippingService):
    def __init__(self, service: ShippingService):
        self.service = service

    # @logging
    def get_rate(self, car_cost: float, tax: int) -> float:

        base_rate = self.service.get_rate(car_cost, tax)
        
        print("Decorator -> Adding the Insurance amt to the final bill")
        insurance_fee = 12000
        return base_rate + insurance_fee

