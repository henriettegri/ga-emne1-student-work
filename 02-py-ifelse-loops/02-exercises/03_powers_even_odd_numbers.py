#potens og partall


number = int(input('Skriv inn et heltall: '))

#opphøyd i andre = squared
squared = number ** 2

#opphøyd i tredje = cubed
cubed = number ** 3

rest = number % 2

print(f'{number} opphøyd i andre er {squared}, og opphøyd i tredje er det {cubed}.')

if rest == 0:
    print('Tallet er et partall.')
else:
    print('Tallet er et oddetall.')