class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.watched = False

    def show_info(self):
        if self.watched == True:
            print(f'{self.title} varer i {self.duration} minutter. Filmen er watched.')
        else:
            print(f'{self.title} varer i {self.duration} minutter. Filmen er Not watched.')

    def mark_watched(self):
        self.watched = True

first_movie = Movie("Big Fish", 96)
second_movie = Movie("Star Wars", 120)

first_movie.mark_watched()
first_movie.show_info()
second_movie.show_info()

print("\n")

movies = [first_movie, second_movie]
for movie in movies:
    movie.show_info()

# Klassen Movie bestemmer hvilke attributter og metoder alle filmobjekter skal ha.
# Alle Movie-objekter har title, duration og watched, samt metodene
# show_info() og mark_watched().

#Attributter lagrer data, metoder utfører handlinger.
#Attributt = hva objektet har, Metode = Hva objektet kan gjøre

# first_movie har verdiene:
# title = "Big Fish"
# duration = 96
# watched = True

# second_movie har verdiene:
# title = "Star Wars"
# duration = 120
# watched = False
