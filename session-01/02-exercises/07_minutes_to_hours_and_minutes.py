# Minutter til timer og minutter
minutes = int(input("Antall minutter: "))

timer = minutes // 60
minutter = minutes % 60

if timer == 1:
    print(f"{minutes} minutter blir {timer} time og {minutter} minutter")
else:
    print(f"{minutes} minutter blir {timer} timer og {minutter} minutter")
