#returnere en boolsk verdi

def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False

for number in range (1, 11):
    check = is_even(number)
    print(number, check)
