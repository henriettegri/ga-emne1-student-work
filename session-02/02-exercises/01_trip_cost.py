#beregn kostaden for en kjøretur

#les inn kjørelengde i km, drivstofforbruk pr 100 km, drivstoffpris pr liter

distance = float(input('Distance in km: '))
fuel_per_100_km = float(input('Fuel per 100 km (liter): '))
fuel_price = float(input('Fuel price: '))

#drivstoffmengde
fuel_amount = distance / 100 * fuel_per_100_km

#kostnad
cost = fuel_amount * fuel_price

print(f'Mengde drivstoff du trenger er {fuel_amount:.2f}. Prisen for drivstoffet blir da {cost:.2f} kr. ')