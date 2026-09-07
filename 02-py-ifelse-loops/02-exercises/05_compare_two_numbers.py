#sammenligne to tall

first_number = int(input('Skriv et heltall: '))
second_number = int(input('Skriv et annet heltall: '))

if first_number == second_number:
    print('Tallene er like.')
elif first_number > second_number:
    print('Det første tallet er større enn det andre.')
else:
    print('Det andre tallet er større enn det første.')