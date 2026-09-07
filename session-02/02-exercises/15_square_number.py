#Kvadrattall

limit = int(input('Skriv en øvre grense:'))

number = 1

while number ** 2 <= limit:
    print(number ** 2)
    number += 1