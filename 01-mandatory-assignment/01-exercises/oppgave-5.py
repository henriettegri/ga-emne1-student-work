from datetime import datetime, timedelta

#validere input etter hva som er gyldig, bruke av while-løkker, try except, importere datetime for datovaldigering

#Aktiviteter
activities = [
    {
        "title": "Tennis",
        "category": "Sport",
        "date": "23.09.2026",
        "estimated_minutes": 45,
        "status": "planned"
    },
    {
        "title": "Football",
        "category": "Sport",
        "date": "20.09.2026",
        "estimated_minutes": 60,
        "status": "planned"
    },
    {
        "title": "Crochet",
        "category": "Hobby",
        "date": "20.09.2025",
        "estimated_minutes": 45,
        "status": "completed"
    },
    ]

def register_and_show_activities():
    valid_title = False
    while not valid_title:

        new_title = input("Legg til emne: ").strip().capitalize()
        if new_title == "":
             print("Emne kan ikke være tomt.")
             continue
        else:
            valid_title = True

    valid_category = False
    while not valid_category:

        new_category = input("Legg til kategori: ").strip().capitalize()
        if new_category == "":
             print("Emne kan ikke være tomt.")
             continue
        else:
            valid_category = True

    valid_date = False
    while not valid_date:

        new_date_input = input("Skriv en dato (dd.mm.åååå): ")

        if new_date_input.strip() == "":
             print("Dato kan ikke være tom.\n")
             continue

        try:
            new_date = datetime.strptime(new_date_input, '%d.%m.%Y')
            valid_date = True
        except ValueError:
            print('Denne datoen er ikke gyldig!\n')

    valid_minutes = False
    while not valid_minutes:
        new_minutes = input("Legg til estimerte minutter: ")

        if new_minutes.strip() == "":
             print("Emne kan ikke være tomt.")
             continue

        try:
            new_minutes = int(new_minutes)

        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')
            continue

        if new_minutes > 0:
            valid_minutes = True

    valid_status = False
    while not valid_status:
        new_status = input("Legg til status: ").lower()

        if new_status == "planned" or new_status == "completed":
            valid_status = True
        else:
            print("Du må skrive planned eller completed.")
            continue

    new_activity = {
        "title": new_title,
        "category": new_category,
        "date": new_date,
        "estimated_minutes": new_minutes,
        "status": new_status
    }

    activities.append(new_activity)
    print(activities)


def search():
    valid_search_1 = False
    while not valid_search_1:
        search_1 = input("Søk etter et tema: ").strip().capitalize()
        if search_1 == "":
            print("Input kan ikke være tomt.")
            continue
        else:
            valid_search_1 = True

    found = False
    for activity in activities:
        if activity["title"] == search_1:
            print(activity)
            found = True

    if not found:
            print("Tema finnes ikke.")

    valid_search_2 = False
    while not valid_search_2:
        search_2 = input("Søk etter et kategori: ").strip().capitalize()
        if search_2 == "":
            print("Input kan ikke være tomt.")
            continue
        else:
            valid_search_2 = True

    found = False
    for activity in activities:
        if activity["category"] == search_2:
            print(activity)
            found = True

    if not found:
            print("Kategori finnes ikke.")




    print("\nListen sortert etter varighet, lengst først:")
    for row in list_of_minutes:
        print(f"ID: {row['id']}, minutter: {row['minutes']}")

def show_menu():
    menu = ["1.Registrere og vise aktiviteter", "2.Søke etter tittel eller kategori", "3.Filtrere etter status.",
            "4.Sortere etter dato eller varighet.", "5.Markere en aktivitet som fullført.",
            "6.Vise antall aktiviteter, samlet estimert tid og antall fullførte.",
            "7.Lagre aktiviteter til fil og lese dem inn igjen.", "8.Avslutte programmet."]
    print(menu[0])
    print(menu[1])
    print(menu[2])
    print(menu[3])
    print(menu[4])
    print(menu[5])
    print(menu[6])
    print(menu[7])


while (True):
    show_menu()
    number = input('Velg et nummer fra menyen:')

    if not number.isdigit():
        print("Ugyldig input, prøv igjen.")
        continue

    number = int(number)

    if number == 1:
        #kalle på en funksjon for å registrere og vise aktivitet
        register_and_show_activities()

    elif number == 2:
        # kalle på en funksjon for å søke etter tittel eller kategori
        search()
    elif number == 3:
        list_of_status = []
        for activity in activities:
            print(f'Status: {activity["status"]}, tittel: {activity["title"]},  kategori: {activity["category"]},  minutter: {activity["estimated_minutes"]} og dato: {activity["date"]}.')


    elif number == 4:
        input_number = False
        while not input_number:
            print("Trykk 1 for å sortere etter varighet.")
            print("Trykk 2 for å sortere etter dato.")
            svar = input("Hva velger du? ")

            if not svar.isdigit():
                print("Ugyldig input, prøv igjen.\n")
                continue

            if svar == "1":
                # sortere etter minutter, prøver å lære meg noe nytt

                sorted_activities = sorted(
                    activities,
                    key=lambda activity:activity["estimated_minutes"],
                    reverse=True
                )

                for activity in sorted_activities:
                    print(activity)
                input_number = True
            else:
                sorted_activities = sorted(
                    activities,
                    key=lambda activity: activity["date"]
                )

                for activity in sorted_activities:
                    print(activity)
                input_number = True



    elif number == 5:
        # kalle på en funksjon for å markere en aktivitet som fullført

    #elif number == 6:
        # kalle på en funksjon for å vise antall aktiviteter, samlet estimert tid og antall fullførte

    #elif number == 7:
        # kalle på en funksjon for å lagre aktiviteter til fil og lese dem inn igjen

    elif number == 8:
        # Avslutte programmet
        break
    else:
        print("Det er et ugyldig valg, prøv igjen!")


class Activity:
    def __init__(self, title, category, date, estimated_minutes, status):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

