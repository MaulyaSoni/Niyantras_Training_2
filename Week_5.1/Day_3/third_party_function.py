class AdvancedShipping:
    
    def cost_after_tax(self, car_cost: int , tax : int) -> float:
        print(f"[SDK] Calculating cost for {car_cost} and tax : {tax}")
        tax = tax / 100
        car_cost += car_cost * tax
        return car_cost
