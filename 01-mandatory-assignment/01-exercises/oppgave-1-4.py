#Beregner tidsbruk på studieøkter, oppgave 1.1
def tidsbruk():
    study_sessions = int(input("Antall studieøkter: "))
    minutes_per_session = int(input("Minutter per økt: "))

    if study_sessions > 0 and minutes_per_session > 0:
        time = study_sessions * minutes_per_session
        hours = time // 60
        minutes = time % 60

        print(f"Samlet tidsbruk: {hours} timer og {minutes} minutter.")

    else:
        print("Feil, prøv igjen!")

#Analyserer tekst, oppgave 1.2
def analyze_text():
    text = input("Skriv et ord eller en setning:")

    if text.isspace() or text == '':
        print("Feil input, prøv igjen!")

    else:
        print(f' Antall bokstaver: {len(text)}')
        print(f' Tekst skrevet med små bokstaver: {text.lower()}')
        print(f' Tekst skrevet baklengs: {text[::-1]}')

        if "python" in text:
            print("Ja, teksten inneholder ordet Python!")
        elif "Python" in text:
            print("Ja, teksten inneholder ordet Python!")
        elif "PYTHON" in text:
            print("Ja, teksten inneholder ordet Python!")
        else:
            print("Nei, teksten inneholder ikke ordet Python!")

#Analysere et tallintervall, oppgave 1.3
def analyze_number():

    valid_input = False
    while not valid_input:
        start_value = input("Skriv en startverdi: ")
        try:
            number_1 = int(start_value)
        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')
            continue

        end_value = input("Skriv en sluttverdi: ")

        try:
            number_2 = int(end_value)

        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')
            continue

        if start_value > end_value:
            print("Ugyldig input, prøv igjen.")
            continue

        valid_input = True

    even = []
    three = []
    total = 0
    for number in range(number_1, number_2 + 1):
        total = total + number

        if number % 2 == 0:
            even.append(number)

        if number % 3 == 0:
            three.append(number)

    print(f'Partall: {even}')
    print(f'Delelig på 3: {three}')
    print(f'Totalt: {total}')

# Vise menyen, sette sammen alle oppgavene, oppgave 1.4
def show_menu():
    menu = ["1.Beregn tidsbruk", "2.Analyser tekst", "3.Analyser tallintervall", "4.Avslutt"]
    print(menu[0])
    print(menu[1])
    print(menu[2])
    print(menu[-1])


while True:
    show_menu()
    number = input('Velg et nummer fra menyen:')

    if not number.isdigit():
        print("Ugyldig input, prøv igjen.")
        continue

    number = int(number)

    if number == 1:
        tidsbruk()

    elif number == 2:
        analyze_text()

    elif number == 3:
        analyze_number()

    elif number == 4:
        break
    else:
        print("Ugyldig input, prøv igjen!")

