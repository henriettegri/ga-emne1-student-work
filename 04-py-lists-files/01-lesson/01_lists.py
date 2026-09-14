guests = ["Kermit", "Miss Piggy", "Gonzo"]
print(guests)

print("\n---\n")

mixed_bag = ["Tomas", 52, True]
print(mixed_bag)

print("\n---\n")

print(guests[0])
print(guests[1])
print(guests[-1])

print("\n---\n")

# legger til et element i lista
guests.append("Animal")
# fjerne et element
guests.remove("Gonzo")
print(guests)

#se antall i lista
print(len(guests))

print("\n---\n")
#for each løkke
for guest in guests:
    print(f"Welcome, {guest}")

print("\n---\n")
scores = [72, 88, 91, 65]
print(len(scores))
print(sum(scores))

average = sum(scores) /len(scores)
print(f"Average :{average}")
print(min(scores))
print(max(scores))

