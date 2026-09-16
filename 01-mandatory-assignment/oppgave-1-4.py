def tidsbruk():
    study_sessions = int(input("Number of sessions: "))
    minutes_per_session = int(input("Minutes per sessions: "))

    if study_sessions > 0 and minutes_per_session > 0:
        time = study_sessions * minutes_per_session
        hours = time // 60
        minutes = time % 60

        print(f"Total study time: {hours} hours and {minutes} minutes.")

    else:
        print("Error, try again!")

def analyze_text():
    text = input("Enter a word or a sentence:")

    if text.isspace() or text == '':
        print("Wrong input, please try again.")

    else:
        print(f' Number of letters: {len(text)}')
        print(f' Text written in lower letters: {text.lower()}')
        print(f' Text reversed: {text[::-1]}')

        if "python" in text:
            print("Yes, python is present!")
        elif "Python" in text:
            print("Yes, python is present!")
        elif "PYTHON" in text:
            print("Yes, python is present!")
        else:
            print("No, python is not present!")

def show_menu():
    menu = ["1.Beregn tidsbruk", "2.Analyser tekst", "3.Analyser tallintervall", "4.Avslutt"]
    print(menu[0])
    print(menu[1])
    print(menu[2])
    print(menu[-1])


while True:
    show_menu()
    number = input('Write a number from the menu:')

    if not number.isdigit():
        print("Ugyldig input, prøv igjen.")
        continue

    number = int(number)

    if number == 1:
        tidsbruk()

    elif number == 2:
        analyze_text()

    elif number == 3:
        analyze_text()

    elif number == 4:
        break
    else:
        print("Invalid input, try again!")

