scoreboard = {
    "Jens": 100,
    "Tommy": 200,
    "Per": 90,
    "James": 150,
    "Hans": 110
}

print(scoreboard["Jens"])
scoreboard["Tommy"] = 250

print(scoreboard)

for navn, poeng in scoreboard.items():
    print(navn, poeng)