# oppgave 1.1
check_1 = False
study_sessions = (input("Number of sessions: "))

while check_1 == False:

    if not study_sessions.isdigit() or int(study_sessions) == 0:
        print("Error, try again!")
        study_sessions = (input("Number of sessions: "))
    else:
        check_1 = True
        check_2 = False

minutes_per_session = input("Minutes per sessions: ")

while check_2 == False:
    if not minutes_per_session.isdigit() or int(minutes_per_session) == 0:
        print("Error, try again!")
    else:
        check_2 = True

time = int(study_sessions) * int(minutes_per_session)
hours = time // 60
minutes = time % 60

print(f"Total study time: {hours} hours and {minutes} minutes.")

