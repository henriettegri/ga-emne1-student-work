#gratis levering
order_amount = 650
is_member = True

if order_amount >= 800 or is_member:
    print('Du får gratis levering.')
else:
    print('Du får ikke gratis levering.')