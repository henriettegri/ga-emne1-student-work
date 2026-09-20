def oppgave1():
    while (True):
        svar = input("Hva er 2+2? ")
        try:
            svarSomTall = int(svar)
        except ValueError:
            print('Feil! Du må skrive inn et tall!\n')
            continue

        if svarSomTall == 4:
            print('Riktig')
            break
        else:
            print('Feil')

def oppgave2():
    print("Oppgave 2")

while(True):
    print("Trykk 1 for oppgave 1.")
    print("Trykk 2 for oppgave 2.")
    print("Trykk 3 for oppgave 3.")
    print("Trykk 4 for avslutt.")

    svar = input("Hva velger du? ")
    if svar == "1":
        oppgave1()
    elif svar == "2":
        oppgave2()
    if svar == "4":
        break

    print(f'Du svarte {svar}')