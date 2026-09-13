#finn det største tallet

def find_largest(first_number, second_number):
    if first_number > second_number:
        return f'{first_number} is largest!'
    elif first_number < second_number:
        return f'{second_number} is largest!'
    else:
        return 'The numbers are the same!'


print(find_largest(6, 2))
print(find_largest(2, 4))
print(find_largest(6, 6))