#Pin-kode med begrenset antall

secret_pin = 2468
attempts_left = 3
is_authenticated = False

while attempts_left > 0 and not is_authenticated:
    code = int(input('Skriv inn pin-koden din:'))
    if code == secret_pin:
        print('Access granted.')
        is_authenticated = True
    else:
        print('Wrong pin-code.')
        attempts_left -= 1
        print(f'Attemptes left: {attempts_left}')

if not is_authenticated:
    print('Access denied.')