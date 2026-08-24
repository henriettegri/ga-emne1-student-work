# Testing user input

name = input("What is your name? ")
course = "Emne 1"

print(f"Hello, {name}!")
print("Hello, " + name + "!")
print("Hello, ", name, "!")

print(f"Welcome to {course}.")

# gjøre om input til tall som kan regnes med (int)
age = int(input("How old are you?"))
next_year = age + 1

print(f"Next year you'll be {next_year}.")