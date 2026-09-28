from abc import ABC, abstractmethod
from third_party_function import AdvancedShipping
from decorators import logging

# interface
class ShippingService(ABC):
    @abstractmethod
    def get_rate(self, car_cost: float, tax: int) -> float:
        pass
