from pathlib import Path
import csv

data_folder = Path(__file__).parent.parent /"data"
path = data_folder/ "supporthenvendelser.csv"

print(path)


try:
    with path.open("r", encoding="utf-8") as file:
        csv_file = csv.DictReader(file)

        # sjekker om radene inneholder verdier
        print('KONTROLLERT DATA:')
        valid_rows = []
        for row_number, row in enumerate(csv_file, start=2):

            if "" in row.values():
                print(f'Rad {row_number}: mangler verdi!')
                continue

            #sjekker om id er et positivt heltall
            try:
                id_category = int(row["id"])
                if id_category <=0:
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
    print(f'\nAntall gyldige rader: {len(valid_rows)}')

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

    print(f'Antall gyldige henvendelser: {len(valid_rows)}.')
    print(f'Antall i hver kategori:\n- Innlogging {category_1}.\n- Programvare: {category_2}.\n- Nettverk: {category_3}.\n- Utstyr: {category_4}.')

    #samlet og gjennomsnittlig tidsbruk
    if len(valid_rows) == 0:
        print("Ingen gyldige henvendelser funnet.")
    else:
        total_minutes = 0

        number_of_cases = 0
        for row in valid_rows:
            total_minutes += int(row["minutes"])
            number_of_cases += 1
        average = total_minutes / number_of_cases
        print(f'\nSamlet tidsbruk: {total_minutes}.')
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

    print(f'\nLøste saker: {solved}.')
    print(f'Uløste saker: {unsolved}.\n')

    #flest henvendelser
    most_cases = max(category_1, category_2, category_3, category_4)
    if most_cases == category_1:
        most_category = "Innlogging"
        print(f"{most_category} er den mest brukte kategorien.")
    elif most_cases == category_2:
        most_category = "Programvare"
        print(f"{most_category} er den mest brukte kategorien.")
    elif most_cases == category_3:
        most_category = "Nettverk"
        print(f"{most_category} er den mest brukte kategorien.")
    else:
        most_category = "Utstyr"
        print(f"{most_category} er den mest brukte kategorien.")

    # sortere etter minutter
    list_of_minutes = []
    for row in valid_rows:
        if row["is_resolved"] == "no":
            list_of_minutes.append(row)

    def get_minutes(row):
        return int(row["minutes"])


    list_of_minutes.sort(key=get_minutes, reverse=True)


    print("\nListen sortert etter varighet, lengst først:")
    for row in list_of_minutes:
        print(f"ID: {row['id']}, minutter: {row['minutes']}")


except FileNotFoundError:
    print(f"Error, could not open file: {path}")

file_path = Path("support-rapport.txt")
with file_path.open("w", encoding="utf-8") as file:
    file.write("SUPPORTRAPPORT")
    file.write("\n------\n")
    file.write("ANALYSERESULTATER\n")

    #antall gyldige henvendelser og antall i hver kategori
    file.write(f"Antall gyldige henvendelser: {len(valid_rows)}\n\n")
    file.write(f"Antall henvendelser i hver kategori:\n")
    file.write(f" - Innlogging: {category_1}.\n")
    file.write(f" - Programvare: {category_2}.\n")
    file.write(f" - Nettverk: {category_3}.\n")
    file.write(f" - Utstyr: {category_4}.\n")

#samlet og gjennomsnittlig tidsbruk, med gjennomsnitt til én desimal
    file.write("\n")
    file.write(f'Samlet tidsbruk: {total_minutes}.\n')
    file.write(f'Gjennomsnittlig tidsbruk: {average:.1f}\n')

#antall løste og uløste henvendelser
    file.write("\n")
    file.write(f'Løste saker: {solved}.\n')
    file.write(f'Uløste saker: {unsolved}.\n')

#kategorien med flest henvendelser
    file.write(f"Kategorien med flest henvendelser: {most_category}\n")

#uløste henvendelser sortert med den mest tidkrevende først
    file.write("\n")
    file.write("Uløste henvendeler:\n")
    for row in list_of_minutes:
        file.write(f"ID: {row['id']}, minutter: {row['minutes']}\n")

print(f"\nFile '{file_path}' created successfully.")