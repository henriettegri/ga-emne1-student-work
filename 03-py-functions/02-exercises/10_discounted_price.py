#Pris etter rabatt

def calculate_discounted_price(price, discount_percent):
    discount = price * (discount_percent/100)
    total = price - discount
    return total

result = calculate_discounted_price(299, 30)
print(f'Den nye prisen blir {result:.2f} kr.')

