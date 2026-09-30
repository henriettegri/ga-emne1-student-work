numbers = [38, 55, 2, 76, 83, 22]

over_fifty_list =[]
count = 0
for number in numbers:
    if number > 50:
        count += 1
        over_fifty_list.append(number)

print(f'Listen inneholder: {count} tall over 50. Tallene er: {over_fifty_list}')

#en annen løsning:
#print(f'Listen inneholder: {len(over_fifty_list)} tall over 50. Tallene er: {over_fifty_list}')
