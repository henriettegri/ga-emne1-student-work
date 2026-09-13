def calculate_tip(amount, tip_percent = 0):
    tip = amount * (tip_percent/100)
    return tip

print(calculate_tip(100))
print(calculate_tip(200, tip_percent = 5))