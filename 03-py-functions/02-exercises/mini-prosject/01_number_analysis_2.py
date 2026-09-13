def read_number():
    number = int(input("Write a number: "))
    return number

def describe_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def show_analyses(number, sign, even):
    print(f'Number: {number}')
    print(f'Sign: {sign}')
    print(f'Even : {even}')

def run_number_analyzer():
    number = read_number()
    sign = describe_sign(number)
    even = is_even(number)

    show_analyses(number, sign, even)

run_number_analyzer()