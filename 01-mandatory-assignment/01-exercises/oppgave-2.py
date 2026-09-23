#Studieøkter
lessons = [
    {
        "topic": "Python",
        "duration_minutes": 45,
        "status": "completed"
    },
    {
        "topic": "Java",
        "duration_minutes": 60,
        "status": "planned"
    },
    {
        "topic": "Html",
        "duration_minutes": 90,
        "status": "planned"
    },
    {
        "topic": "C++",
        "duration_minutes": 30,
        "status": "completed"
    },
    {
        "topic": "MySQL",
        "duration_minutes": 120,
        "status": "planned"
    },
    ]

#Legge til økter
def add_lessons():
    while (True):

        new_topic = input("Legg til emne: ").strip().capitalize()
        if new_topic == "":
             print("Emne kan ikke være tomt.")
             continue
        else:
            break


    while (True):
        new_duration_minutes = input("Legg til varighet: ")

        if new_duration_minutes.strip() == "":
             print("Emne kan ikke være tomt.")
             continue

        try:
            svarSomTall = int(new_duration_minutes)

        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')
            continue

        if svarSomTall > 0:
            break

    while (True):
        new_status = input("Legg til status: ")

        if new_status == "planned" or new_status == "completed":
            break
        else:
            print("Du må skrive planned eller completed.")
            continue

    lessons = {
        "topic": new_topic,
        "duration_minutes": new_duration_minutes,
        "status": new_status
    }

    print(lessons)

#Søke
def search():
    while True:
        search = input("Søk etter et tema: ").strip().capitalize()
        if search == "":
             print("Input kan ikke være tomt.")
             continue
        else:
            break

    for lesson in lessons:
        if lesson["topic"] == search:
            print(lesson)

#Finne varighet
def get_duration(lesson):
    return lesson["duration_minutes"]

#Finne sum og gjennomsnitt
def total_average():
    total_minutes = 0
    completed_count = 0
    for lesson in lessons:
        if lesson["status"] == "completed":
            total_minutes += lesson["duration_minutes"]
            completed_count += 1
            average = total_minutes / completed_count

    return total_minutes, average


#Vise meny
while True:
    print("Trykk 1 for å registrere studieøkt.")
    print("Trykk 2 for å vise alle studieøkter.")
    print("Trykk 3 for å vise alle fullførte stuideøkter.")
    print("Trykk 4 for å søke etter tema.")
    print("Trykk 5 for å sortere etter varighet .")
    print("Trykk 6 for å vise statistikk.")
    print("Trykk 7 for avslutt.")

    svar = input("Hva velger du? ")

    if not svar.isdigit():
        print("Ugyldig input, prøv igjen.\n")
        continue

    if svar == "1":
        add_lessons()

    elif svar == "2":
            print(lessons)

    elif svar == "3":
        for lesson in lessons:
            if lesson["status"] == "completed":
                print(lesson)

    elif svar == "4":
        search()

    elif svar == "5":
        lessons.sort(key=get_duration, reverse = True)
        print(lessons)

    elif svar == "6":
        total_minutes, average = total_average()
        print(f'Total varighet: {total_minutes}. Gjennomsnitt: {average:.2f}')

    if svar == "7":
        break

    print(f'Du valgte {svar}\n')