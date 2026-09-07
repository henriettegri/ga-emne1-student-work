def greet(name, greeting = "Hello"):
    print(f'{greeting}, {name}!')
#greeting er en defaultverdi, den kan overstyres.

greet('Erna')
greet('Jonas', greeting = 'Good morning')
#greeting =  kan sløyfes i Jonas