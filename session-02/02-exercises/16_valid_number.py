#Gyldig nummer

valid_number = 0

while valid_number <= 0 :
    valid_number = int(input("Skriv et positivt heltall: "))

#husk at programmet skal fortsette så lenge tallene er ugyldige.
#Alle tall fra null og under er ugyldige, derfor må betingelsene være
#<= 0 som betyr minddre eller = 0. 