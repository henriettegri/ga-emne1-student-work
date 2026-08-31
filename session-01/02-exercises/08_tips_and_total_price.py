# Tips og totalpris

price = int(input("Skriv inn pris:"))

tips = price * (15 / 100)
total_price = price + tips

print(f'Totalpris med 15 % tips blir {total_price} kr.')
