from abc import ABC, abstractmethod
from third_party_function import AdvancedShipping

class ShippingService(ABC):
    @abstractmethod
    def get_rate(self, car_cost: float, tax: str) -> float:
        pass

class ShippingAdapter(ShippingService):
    def __init__(self, sdk: AdvancedShipping):
        self.sdk = sdk

    def get_rate(self, car_cost: float, tax: str) -> float:

        print("converting price of car from USD to INR")
        
        car_cost = int(car_cost * 92)

        print("Cost in INR : ",car_cost)
        print("Interface transformation: Calls 'calculate_total_cost' instead of 'get_rate' ")
        
        return self.sdk.cost_after_tax(car_cost, tax)

class InsuranceDecorator(ShippingService):
    def __init__(self, service: ShippingService):
        self.service = service

    def get_rate(self, car_cost: float, tax: int) -> float:

        base_rate = self.service.get_rate(car_cost, tax)
        
        print("[Decorator] Injecting premium insurance surcharges.")
        insurance_fee = 12000
        return base_rate + insurance_fee
