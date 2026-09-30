spaceship = {
    "name": "Battlestar Galactica",
    "captain": "Adama",
    "speed": "fast",
    "operational": "yes"
}

print(f'Romskip: {spaceship["name"]} og kaptein: {spaceship["captain"]}')

#endre noe i dict
spaceship["speed"] = "slow"

#legge til noe i dict
spaceship["universe"] = "Caprica"
print(spaceship)