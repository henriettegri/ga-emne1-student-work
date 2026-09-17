while True:
    start_value = int(input("Write a start value: "))
    end_value = int(input("Write a end value: "))

    if start_value > end_value:
        print("Ugyldig input, prøv igjen.")
        continue

    break

even = []
three = []
total = 0
for number in range (start_value, end_value+1):
    total = total + number

    if number % 2 == 0:
        even.append(number)

    if number % 3 == 0:
        three.append(number)

print(f'Even numbers: {even}')
print(f'Divisible by three: {three}')
print(f'Total: {total}')



