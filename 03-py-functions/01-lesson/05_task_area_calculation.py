def calculate_area(width, height):
    area = width * height
    return  area

total_area = calculate_area(5, 8)
print(f'Total area is: {total_area:.2f}')

#for tre forskjellige
total_area = 0
for width in range (2, 5):
    area = calculate_area(width, 2)
    print(f'Area is: {area}')

print(f'Total area is: {total_area}')