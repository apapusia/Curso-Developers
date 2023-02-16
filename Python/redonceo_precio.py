
def pretty_price(price, cents):
    #separar la parte entera del precio
    if isinstance(cents,int):
        cents=cents/100
    
    return int(price)+cents
           
print(pretty_price(34.23, 0.99))
        