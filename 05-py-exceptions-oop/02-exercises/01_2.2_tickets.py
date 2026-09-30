tickets = input("Hvor mange billetter ønsker du:")

try:
    svarsomtall = int(tickets)
    if svarsomtall > 0 and svarsomtall <=8:
        total = svarsomtall * 120
        print(f'{svarsomtall} billetter koster {total}.')
    else:
        print("Du kan ikke bestille flere enn 8 billetter.")
except ValueError:
    print("Antall billetter må være et heltall.")