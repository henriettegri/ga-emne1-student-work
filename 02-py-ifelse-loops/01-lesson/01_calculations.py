numbers_of_tickets = int(input('How many tickets? '))
ticket_price = 180
service_fee = 35

subtotal = ticket_price * numbers_of_tickets
total = subtotal + service_fee
price_per_person = total / numbers_of_tickets

print(total)
print(f"{price_per_person:.2f}")

#print(round(price_per_person)) - runde av

#sum = sum + 1
#sum +=1 De to betyr det samme