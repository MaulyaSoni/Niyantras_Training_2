from third_party_function import AdvancedShipping
from core import ShippingService, InsuranceDecorator , ShippingAdapter

def main():
    print("Without facade and the decorator class approach ")
    obj = AdvancedShipping()

    adapted_shipping = ShippingAdapter(obj)

    insured_shipping = InsuranceDecorator(adapted_shipping)

    car_cost = int(input("Enter the cost of car in USD :- "))
    tax = int(input("\nEnter the percentage of tax :-"))
    final_cost =  adapted_shipping.get_rate(car_cost, tax)
    
    result = {
        "cost_of_car": car_cost,
        "tax": tax,
        "cost_of_car_after_tax":final_cost 
    }

    print("Client Received Manifest Output:")
    print(result)

if __name__ == "__main__":
    main()
