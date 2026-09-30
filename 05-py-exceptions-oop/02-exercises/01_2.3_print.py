try:
    minutes = int(input("Minutes: "))
except ValueError:
    print("Please enter a whole number.")
else:
    print(f"Seconds: {minutes * 60}")
    print("Finished")