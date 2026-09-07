#sammenligne tall

first_number = int(input('Skriv inn et heltall: '))
second_number = int(input('Skriv inn et annet heltall: '))

total = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
division = first_number / second_number
integer_division = first_number // second_number
remainder = first_number % second_number

print(f'Summen av de to tallene er {total}.')
print(f'Differansen av de to tallene er {difference}.')
print(f'Produktet av de to tallene er {product}.')
print(f'Kvotienten av de to tallene er {division:.2f}.')
print(f'Svaret i heltallsdivisjonen av de to tallene er {integer_division}.')
print(f'Rest etter divisjon av de to tallene er {remainder:}.')