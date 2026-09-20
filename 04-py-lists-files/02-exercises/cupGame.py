import random

cups = ["🥛", "🪙", "🥛",]

print("\nVelkommen til koppespiller\n")

print("Blander koppene..")

for i in range(3):
    index1 = random.randint(0, 2)
    index2 = random.randint(0, 2)
    cups[index1], cups[index2] = cups[index2], cups[index1]


#Lar brukeren gjette hvilken kopp som har mynten
guess = int(input("Gjett hvilken kopp som har mynten (0, 1 eller 2): "))

if cups[guess] == "🪙":
    print("Gratulerer! du gjettet riktig!")
else:
    print("Beklager, du gjettet feil. Prøv igjen!")

#Vise fasit
print(f'Fasit: {cups}')



