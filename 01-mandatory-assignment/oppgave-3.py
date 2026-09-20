import datetime


#en funksjon som tar imot en dato på formatet dd.mm.åååå og returnerer en datoverdi når teksten er gyldig
def get_date():
    while True:
        day = input("Skriv en dato på formatet dd: ")

        if day.strip() == "":
             print("Emne kan ikke være tomt.")
             continue

        try:
            day_number = int(day)

        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')
            continue

        if day_number > 0 and day_number <= 31:
            break

    while True:
        month = input("Skriv en måned på formatet mm: ")

        if month.strip() == "":
            print("Emne kan ikke være tomt.")
            continue

        try:
            month_number = int(month)

        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')
            continue

        if month_number > 0 and month_number <= 12:
            break

    while True:
        year =  input("Skriv et år på formatet åååå: ")

        if year.strip() == "":
            print("Emne kan ikke være tomt.")
            continue

        try:
            year_number = int(year)

        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')
            continue

        if year_number > 0:
            break

    x = datetime.datetime(year_number, month_number, day_number)
    print(x)

def get_time():
    while True:
        time = input("Skriv en starttid på formatet hh:mm: ")

        try:
            start_time = datetime.strftime(time, "%H:%M")
            return start_time
        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')


get_date()
start_time = get_time()
print(f'Starttid: {start_time}')





#en funksjon som tar imot starttidspunkt og minutter og returnerer sluttid


#en funksjon som tar imot to datoer og returnerer positivt antall dager mellom dem


#en funksjon som tar imot en list med datoer og returnerer en kronologisk sortert list