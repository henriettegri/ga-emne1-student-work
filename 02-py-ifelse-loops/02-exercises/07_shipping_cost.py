#Beregne fraktkostnader

weight = int(input('Skriv inn vekt på pakken i kg: '))

if weight <= 2:
    print('Frakten blir 79 kroner.')
elif weight <=5:
    print('Frakten blir 129 kroner.')
elif weight <=10:
    print('Frakten blir 199 kroner.')
else:
    print('Pakken er for tung og kan ikke sendes med tjenesten.')

# under er første forsøk med unødvendig mange betingelser. 
#if weight <= 2:
#   print('Frakten blir 79 kroner.')
#elif weight > 2 and weight <=5:
#    print('Frakten blir 129 kroner.')
#elif weight > 5 and weight <=10:
#   print('Frakten blir 199 kroner.')
#else:
#   print('Pakken er for tung og kan ikke sendes med tjenesten.')