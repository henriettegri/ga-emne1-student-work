total = 0
for number in range(1, 11):
    total += number
    print(total)


    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False


    def divisible_by_three(number):
        if number % 3 == 0:
            return True
        else:
            return False


    while True:
        start_value = int(input("Write a start value: "))
        end_value = int(input("Write a end value: "))

        if start_value > end_value:
            print("Ugyldig input, prøv igjen.")

        for number in range(start_value, end_value + 1):
            check_1 = is_even(number)
            check_2 = divisible_by_three(number)
            total = sum(number)

            if check_1 == True:
                print(f'Partall: {number}')
                continue

            if check_2 == True:
                print(f'Delelig med 3: {number}')
                continue

            print(total)



