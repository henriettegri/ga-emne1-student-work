from pathlib import Path
import csv

from unicodedata import category

data_folder = Path(__file__).parent.parent /"data"
path = data_folder/ "supporthenvendelser.csv"

print(path)


try:
    with path.open("r", encoding="utf-8") as file:
        csv_file = csv.DictReader(file)

        # sjekker om radene inneholder verdier

        valid_rows = []
        for row_number, row in enumerate(csv_file, start=2):

            if "" in row.values():
                print(f'Rad {row_number}: mangler verdi!')
                continue

            #sjekker om id er et positivt heltall
            try:
                id = int(row["id"])
                if id <=0:
                    print(f'Rad {row_number}: inneholder ikke et positivt heltall!')
                    continue
            except ValueError:
                print(f'Rad {row_number}: inneholder ikke et tall!')
                continue

            #sjekke at minutes er et heltall på null eller mer
            try:
                minutes = int(row["minutes"])
                if minutes < 0:
                    print(f'Rad {row_number}: minutter kan ikke være negativ!')
                    continue
            except ValueError:
                print(f'Rad {row_number}: Minutter er ikke et tall!')
                continue

            #sjekke at is_resolved er yes eller no
            if row["is_resolved"] != "yes" and row["is_resolved"] != "no":
                print(f'Rad {row_number} må være yes eller no.')
                continue

            valid_rows.append(row)
    # under er en check for at det blir riktig
    #print("Gyldige rader:")
    #for row in valid_rows:
        #print(row)

    #antall gyldige rader
    print(len(valid_rows))

    category_1 = 0

    for row in valid_rows:
        if row["category"] == "innlogging":
                category_1 += 1

    category_2 = 0

    for row in valid_rows:
        if row["category"] == "programvare":
            category_2 += 1

    category_3 = 0

    for row in valid_rows:
        if row["category"] == "nettverk":
            category_3 += 1

    category_4 = 0

    for row in valid_rows:
        if row["category"] == "utstyr":
            category_4 += 1

    print(f'Antall gyldige henvendelser: {valid_rows}.')
    print(f'Antall i hver kategori:\nInnlogging {category_1}.\nProgramvare: {category_2}.\nNettverk: {category_3}.\nUtstyr: {category_4}.')

    #samlet og gjennomsnittlig tidsbruk
    total_minutes = 0
    number_of_cases = 0
    for row in valid_rows:
        total_minutes += int(row["minutes"])
        number_of_cases += 1
        average = total_minutes / number_of_cases
    print(f'Samlet tidsbruk: {total_minutes}.')
    print(f'Gjennomsnittlig tidsbruk: {average:.1f}')

    #løste og uløste saker

    solved = 0
    for row in valid_rows:
        if row["is_resolved"] == "yes":
                solved += 1

    unsolved = 0
    for row in valid_rows:
        if row["is_resolved"] == "no":
            unsolved += 1

    print(f'Løste saker: {solved}.')
    print(f'Uløste saker: {unsolved}.')

    #flest henvendelser
    most_cases = max(category_1, category_2, category_3, category_4)
    if most_cases == category_1:
        print("Innlogging er mest brukt.")
    elif most_cases == category_2:
        print("Programvare er mest brukt.")
    elif most_cases == category_3:
        print("Nettverk er mest brukt.")
    else:
        print("Utstyr er mest brukt.")

    # sortere etter minutter
    list_of_minutes = []
    for row in valid_rows:
        if row["is_resolved"] == "no":
            list_of_minutes.append(row)

    def get_minutes(row):
        return int(row["minutes"])


    list_of_minutes.sort(key=get_minutes, reverse=True)


    print("Listen sortert etter varighet, lengst først")
    for row in list_of_minutes:
        print(row)


except FileNotFoundError:
    print(f"Error, could not open file: {path}")
