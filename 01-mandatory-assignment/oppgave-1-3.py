while True:
    start_value = input("Write a start value: ")
    try:
        number_1 = int(start_value)
    except ValueError:
        print('Feil! Du må skrive inn et tall!\n')
        continue

    end_value = input("Write a end value: ")

    try:
        number_2 = int(end_value)
    except ValueError:
        print('Feil! Du må skrive inn et tall!\n')
        continue

    if start_value > end_value:
        print("Ugyldig input, prøv igjen.")
        continue

    break

even = []
three = []
total = 0
for number in range (number_1, number_2+1):
    total = total + number

    if number % 2 == 0:
        even.append(number)

    if number % 3 == 0:
        three.append(number)

print(f'Even numbers: {even}')
print(f'Divisible by three: {three}')
print(f'Total: {total}')



