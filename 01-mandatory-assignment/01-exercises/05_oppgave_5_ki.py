import json
from datetime import datetime


class Activity:
    def __init__(self, title, category, date, estimated_minutes,
                 status="planned"):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def mark_completed(self):
        self.status = "completed"

    def show_info(self):
        print(
            f"{self.title} | {self.category} | {self.date} | "
            f"{self.estimated_minutes} min | {self.status}"
        )

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "date": self.date,
            "estimated_minutes": self.estimated_minutes,
            "status": self.status
        }


def read_non_empty_text(message):
    while True:
        text = input(message).strip()

        if text:
            return text

        print("Feltet kan ikke være tomt.")


def read_date():
    while True:
        date = input("Dato (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Ugyldig dato. Bruk formatet YYYY-MM-DD.")


def read_minutes():
    while True:
        try:
            minutes = int(input("Estimert varighet i minutter: "))

            if minutes > 0:
                return minutes

            print("Varigheten må være større enn 0.")

        except ValueError:
            print("Skriv inn et heltall.")


def add_activity(activities):
    title = read_non_empty_text("Tittel: ")
    category = read_non_empty_text("Kategori: ")
    date = read_date()
    minutes = read_minutes()

    activity = Activity(title, category, date, minutes)
    activities.append(activity)

    print("Aktivitet registrert.")


def show_activities(activities):
    if not activities:
        print("Ingen aktiviteter registrert.")
        return

    for number, activity in enumerate(activities, start=1):
        print(f"{number}. ", end="")
        activity.show_info()


def search_activities(activities):
    search_text = input(
        "Søk etter tittel eller kategori: "
    ).lower()

    found = False

    for activity in activities:
        if (search_text in activity.title.lower() or
                search_text in activity.category.lower()):
            activity.show_info()
            found = True

    if not found:
        print("Ingen treff.")


def filter_status(activities):
    status = input(
        "Velg status (planned/completed): "
    ).lower()

    found = False

    for activity in activities:
        if activity.status == status:
            activity.show_info()
            found = True

    if not found:
        print("Ingen aktiviteter med denne statusen.")


def sort_activities(activities):
    choice = input(
        "Sorter etter (date/minutes): "
    ).lower()

    if choice == "date":
        sorted_list = sorted(
            activities,
            key=lambda activity: activity.date
        )

    elif choice == "minutes":
        sorted_list = sorted(
            activities,
            key=lambda activity: activity.estimated_minutes
        )

    else:
        print("Ugyldig valg.")
        return

    for activity in sorted_list:
        activity.show_info()


def complete_activity(activities):
    if not activities:
        print("Ingen aktiviteter registrert.")
        return

    show_activities(activities)

    while True:
        try:
            choice = int(input(
                "Hvilken aktivitet er fullført? "
            ))

            if 1 <= choice <= len(activities):
                activities[choice - 1].mark_completed()
                print("Aktiviteten er markert som fullført.")
                return

            print("Velg et gyldig nummer.")

        except ValueError:
            print("Skriv inn et tall.")


def show_statistics(activities):
    total_activities = len(activities)

    total_minutes = sum(
        activity.estimated_minutes
        for activity in activities
    )

    completed = sum(
        1
        for activity in activities
        if activity.status == "completed"
    )

    print(f"Antall aktiviteter: {total_activities}")
    print(f"Samlet estimert tid: {total_minutes} minutter")
    print(f"Antall fullførte: {completed}")


def save_to_file(activities, filename):
    data = []

    for activity in activities:
        data.append(activity.to_dict())

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Data lagret.")


def load_from_file(filename):
    activities = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                activities.append(
                    Activity(
                        item["title"],
                        item["category"],
                        item["date"],
                        item["estimated_minutes"],
                        item["status"]
                    )
                )

        print("Data lastet inn.")

    except FileNotFoundError:
        print(
            "Ingen datafil funnet. Starter med tom liste."
        )

    return activities


def show_menu():
    print("\n--- AKTIVITETSPLANLEGGER ---")
    print("1. Registrer aktivitet")
    print("2. Vis aktiviteter")
    print("3. Søk")
    print("4. Filtrer status")
    print("5. Sorter")
    print("6. Marker som fullført")
    print("7. Statistikk")
    print("8. Lagre")
    print("9. Avslutt")


def main():
    filename = "activities.json"

    activities = load_from_file(filename)

    while True:
        show_menu()

        choice = input("Valg: ")

        if choice == "1":
            add_activity(activities)

        elif choice == "2":
            show_activities(activities)

        elif choice == "3":
            search_activities(activities)

        elif choice == "4":
            filter_status(activities)

        elif choice == "5":
            sort_activities(activities)

        elif choice == "6":
            complete_activity(activities)

        elif choice == "7":
            show_statistics(activities)

        elif choice == "8":
            save_to_file(activities, filename)

        elif choice == "9":
            save_to_file(activities, filename)
            print("Programmet avsluttes.")
            break

        else:
            print("Ugyldig menyvalg.")


main()