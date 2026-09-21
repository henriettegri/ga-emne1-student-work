inputok = False
#Hvis variablen er definert på utsiden av løkka, virker den begge steder
age = 0
while not inputok:

    try:
        age = int(input("Age: "))
    except ValueError:
        print("Error: Only integers are valid!")
    else:
        inputok = True

print(f"Next year: {age + 1}")

print("Done")

