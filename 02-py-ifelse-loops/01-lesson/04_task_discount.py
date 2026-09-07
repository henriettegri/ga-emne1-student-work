amount = float(input('Purchase amount: '))

if amount >= 1000:
    discount = 0.20
elif amount >= 500:
    discount = 0.10
else:
    discount = 0

discountet_amount = amount * (1 - discount)
print(f"Final amount: {discountet_amount:.2f}")
