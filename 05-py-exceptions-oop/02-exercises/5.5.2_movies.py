class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print(f'Tittel: {self.title} og varighet: {self.duration}.')

first_movie = Movie("Big Fish", 96)
second_movie = Movie("Star Wars", 120)

first_movie.show_info()
second_movie.show_info()

second_movie.duration = 130
first_movie.show_info()
second_movie.show_info()
