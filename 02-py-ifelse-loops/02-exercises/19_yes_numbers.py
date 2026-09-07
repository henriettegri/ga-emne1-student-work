#Finn tall som oppfyller flere krav

count = 0
for number in range (1, 101):
    if number % 3 == 0 and number > 20 and number < 80:
        print(number)
        count += 1

print(f' Antall tall som oppfyller kravene: {count} ')