#positivt, negativt eller null - if-løkke inne i if-løkka

number = int(input('Skriv et heltall:'))


if number != 0:
    if number > 0 and number % 2 == 0:
        print('Tallet er positivt. Tallet er et partall.')
    elif number > 0 and number % 2 != 0:
        print('Tallet er positivt. Tallet er et oddetall.')
    elif number < 0 and number % 2 == 0:
        print('Tallet er negativt. Tallet er et partall.')
    else:
        print('Tallet er negativt. Tallet er et oddetall.')

else:
    print('Tallet er null.')