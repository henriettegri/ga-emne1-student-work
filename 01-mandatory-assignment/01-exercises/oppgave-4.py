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


except FileNotFoundError:
    print(f"Error, could not open file: {path}")
