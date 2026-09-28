from interface import ShippingService

#Target :- , want amt converted in INR 
class InsuranceDecorator(ShippingService):
    def __init__(self, service: ShippingService):
        self.service = service

    # @logging
    def get_rate(self, car_cost: float, tax: int) -> float:

        base_rate = self.service.get_rate(car_cost, tax)
        # print("\nDecorator -> Adding the Insurance amt to the final bill\n")
        insurance_fee= int(input("Enter the insurance fee which is applicable "))
        return base_rate + insurance_fee