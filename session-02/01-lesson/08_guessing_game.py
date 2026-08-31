secret_number = 21
attempts_left = 5
guessed_correctly = False
#Add loops thats counts down, then if-else guess logic
#While loop
while attempts_left > 0 and guessed_correctly != True:
#while attempts_left > 0 and not guessed_correctly:
    # Input from user
    guess = int(input('Guess the number: (1-30) '))
# If-else logic
    if guess == secret_number:
        print('Correct!')
        guessed_correctly = True
    elif guess < secret_number:
        print("Too low!")
    else:
        print('Too high!')
    attempts_left -= 1



if not guessed_correctly:
    print(f'Then number was {secret_number}.')
