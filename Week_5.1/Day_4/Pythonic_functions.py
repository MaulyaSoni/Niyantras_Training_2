def calculate_discount(total , discount):
    discount = discount
    disc_temp = discount / 100
    disc_temp *= total
    discounted_total = total - disc_temp
    return discounted_total

def regular_customer(items , total):
    result  = calculate_discount(total , 5)
    return ("Regular Customer : ",result ,  "items :", items)

def member_customer(items , total):
    result  = calculate_discount(total , 10)
    return ("Member Customer : ",result ,  "items :", items)

def vip_customer(items , total):
    result  = calculate_discount(total , 15)
    return ("VIP Customer : ",result , "items :", items)

def switch_customer_type(val : str) ->str :
    if val.lower() == "regular":
        customer = "regular"
    elif val.lower() == "member":
        customer = "member"
    elif val.lower() == "vip":
        customer = "vip"
    else:
        return "Invalid Input of Customer type"
    return customer

def get_bill(items , total , customer):
    if customer == "regular":
        result = regular_customer(items , total)
    elif customer == "member":
        result = member_customer(items , total)    
    elif customer == "vip":
        result = vip_customer(items , total)
    else:
        return "Invalid Input of Customer type"
    
    return (f"{customer} :- {result}")

