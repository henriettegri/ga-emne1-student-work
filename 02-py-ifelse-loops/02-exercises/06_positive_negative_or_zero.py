#positivt, negativt eller null

number = int(input('Skriv et heltall:'))

if number > 0:
    print('Tallet er positivt.')
elif number < 0:
    print('Tallet er negativt.')
else:
    print('Tallet er null.')

if number != 0:
    if number % 2 == 0:
        print('Tallet er et partall.')
    else:
        print('Tallet er et oddetall.')