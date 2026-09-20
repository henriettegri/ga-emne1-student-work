temperatures = [-1, 4, 11, 14, 11, 15, 5]
min = min(temperatures)
max = max(temperatures)
average = sum(temperatures)/len(temperatures)

print("\n---\n")
cold_days = []
for temperature in temperatures:
    print(f"{temperature} degrees.")
    if temperature < 10:
        cold_days.append(temperature)

print(f"Cold days: {cold_days}")
print(f'Minimum: {min}, maximum: {max}, average: {average:.2f}')
