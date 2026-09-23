from datetime import datetime, timedelta

#en funksjon som tar imot en dato på formatet dd.mm.åååå og returnerer en datoverdi når teksten er gyldig
def get_date():
    while True:
        date_input = input("Skriv en dato (dd.mm.åååå): ")

        if date_input.strip() == "":
             print("Dato kan ikke være tom.")
             continue

        try:
            date = datetime.strptime(date_input, '%d.%m.%Y')
            return date
        except ValueError:
            print('Denne datoen er ikke gyldig!')


#en funksjon som tar imot starttidspunkt og minutter og returnerer sluttid
def get_endtime():
    while True:
        start_time = input("Skriv en starttid (HH:mm): ")

        try:
            start_time = datetime.strptime(start_time, "%H:%M")
            break
        except ValueError:
            print('Klokkeslettet er ugyldig, prøv igjen!')

    while True:
        minutes = input("Hvor mange minutter skal du studere?: ")
        if minutes.isdigit() and int(minutes)>0:
            break
        else:
            print("Antall minutter må være et tall og mer enn null, prøv igjen!")

    start = start_time
    end_time = start + timedelta(minutes=int(minutes))
    return end_time

#en funksjon som tar imot to datoer og returnerer positivt antall dager mellom dem
def days_between():
    while True:
        first_date_input = input("Skriv inn første dato (dd.mm.åååå): ")

        try:
            first_date_input = datetime.strptime(first_date_input, "%d.%m.%Y")

            break
        except ValueError:
            print("Denne datoen er ikke gyldig, prøv igjen!")

    while True:
        second_date_input = input("Skriv inn andre dato (dd.mm.åååå): ")

        try:
            second_date_input = datetime.strptime(second_date_input, "%d.%m.%Y")
            break
        except ValueError:
            print("Denne datoen er ikke gyldig, prøv igjen!")


    number_of_days = (second_date_input - first_date_input).days
    #abs i tilfellet antall dager blir negativt.
    return abs(number_of_days)

#get_date()
#get_endtime()
#print(f'Antall dager: {days_between()}')

#en funksjon som tar imot en list med datoer og returnerer en kronologisk sortert list
def list_of_dates(date_list):
    date_list.sort()
    return date_list

#Hovedprogram
print('STUDIEØKT')
study_date = get_date()
print(f'Dato: {study_date.strftime("%d.%m.%Y")}')
#legg inn sluttid
end_time = get_endtime()
print(f'Studieøkten slutter kl: {end_time.strftime("%H:%M")}')

#beregne antall dager mellom
print('\nDatoanalyse')
number_of_days = days_between()
print(f'Antall dager mellom datoene: {number_of_days}')

#Lage en liste med datoer
print('\nSortere datoer')
date_list = []
day_1 = get_date()
day_2 = get_date()
day_3 = get_date()

date_list.append(day_1)
date_list.append(day_2)
date_list.append(day_3)

#sortere datoene
sorted_dates = list_of_dates(date_list)

#skrive ut resultatene
print(f'\nSorterte datoer:')
for date in sorted_dates:
    print(date.strftime("%d.%m.%Y"))