# Totalpris

product = input('Skriv inn produktnavn: ')
pris = float(input('Skriv inn enhetpris: '))
antall = int(input('Skriv inn antall: '))

total_pris = pris * antall

print(f'{antall} stk {product} koster totalt {total_pris:.2f} kr.')