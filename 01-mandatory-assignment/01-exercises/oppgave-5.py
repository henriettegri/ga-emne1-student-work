#validere input etter hva som er gyldig, bruke av while-løkker, try except, importere datetime for datovaldigering

def show_menu():
    menu = ["1.Registrere og vise aktiviteter", "2.Søke etter tittel eller kategori", "3.Filtrere etter status.", "4.Sortere etter dato eller varighet.", "5.Markere en aktivitet som fullført.", "6.Vise antall aktiviteter, samlet estimert tid og antall fullførte.", "7.Lagre aktiviteter til fil og lese dem inn igjen.", "8.Avslutte programmet."]
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
        #register_and_show_acticities()

    elif number == 2:
        # kalle på en funksjon for å søke etter tittel eller kategori

    elif number == 3:
        # kalle på en funksjon for å filtrere etter status

    elif number == 4:
        # kalle på en funksjon for å sortere etter dato eller varighet

    elif number == 5:
        # kalle på en funksjon for å markere en aktivitet som fullført

    elif number == 6:
        # kalle på en funksjon for å vise antall aktiviteter, samlet estimert tid og antall fullførte

    elif number == 7:
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

