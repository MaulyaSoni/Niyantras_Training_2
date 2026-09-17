from third_party_function import AdvancedShipping
from core import ShippingService, InsuranceDecorator , ShippingAdapter
from facade import ShippingFacade

def main():
    print("Without facade and the decorator class approach")

    obj = AdvancedShipping()
    adapted_shipping = ShippingAdapter(obj)
    insured_shipping = InsuranceDecorator(adapted_shipping)

    car_cost = int(input("Enter the cost of car in USD :- "))
    tax = int(input("\nEnter the percentage of tax :-"))
    final_cost =  insured_shipping.get_rate(car_cost, tax)
    
    result = {
        "cost_of_car": car_cost,
        "tax": tax,
        "cost_of_car_after_tax":final_cost 
    }

    print(result)
    
#-----------------------------------------------------------------------------------------------

    print("\n\nDataClass with the facade approach ")

    obj1 = AdvancedShipping()
    adapted_ship = ShippingAdapter(obj1)
    insured_ship = InsuranceDecorator(adapted_ship)

    car_cost_1 = int(input("Enter the cost of car in USD :- "))
    tax1 = int(input("\nEnter the percentage of tax :-"))
  
    facade_orch = ShippingFacade(insured_ship, obj1)

    res = facade_orch.final(car_cost_1 , tax1)
    
    print(res)
    
if __name__ == "__main__":
    main()
