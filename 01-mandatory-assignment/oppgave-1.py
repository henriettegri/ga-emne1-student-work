# oppgave 1.1
study_sessions = int(input("Number of sessions: "))
minutes_per_session = int(input("Minutes per sessions: "))

if study_sessions > 0 and minutes_per_session > 0:
    time = study_sessions * minutes_per_session
    hours = time // 60
    minutes = time % 60

    print(f"Total study time: {hours} hours and {minutes} minutes.")

else:
    print("Error, try again!")



