# *Create a class for representing a movie with some attributes (title, director, duration, actors, rating)
# and behavior (find if movie director name starts with specific symbol, find if some person is an actor, change rating),
# create several movies and perform operations on them, check how many movies are created

# Создайте класс для представления фильма с некоторыми атрибутами (название, режиссер, продолжительность,
# актеры, рейтинг) и поведением (найдите, начинается ли имя режиссера с определенного символа, выясните,
# является ли какой-то человек актером, измените рейтинг),
# создайте несколько фильмов и производите над ними операции, проверяйте, сколько фильмов создано

class Movie:
    def __init__(self, title, director, duration, actors, rating):
        self.title = title
        self.director = director
        self.duration = duration
        self.actors = actors
        self.rating = rating

    def name_started(self, symbol):
        if self.director[0] == symbol:
            print("yes")
        else:
            print("No")

    def raiting(self, raiting):
        self.rating += raiting

    def name_actors(self, name):
        if name in self.actors:
            print("yes")
        else:
            print("no")

    def show(self):
        print("title -" + self.title, "\n", "director - " + str(self.director), "\n",
              "duration - " + str(self.duration), "\n",
              "actors - " + str(self.actors), "\n", "rating - " + str(self.rating))


print("_________movie 1 _______")
movie_1 = Movie("farsazh", "A.VHgjkh", 120, ["Nike", "Devid", "Emm"], 546)
movie_1.show()
print("_________direct name started_______")
movie_1.name_started("A")
print("_________movie 2_______")
movie_2 = Movie("farsazh 2", "Abfd.VHgjkh", 150, ["A.Gresgh", "Ina", "Dima"], 650)
movie_2.show()
print("_________new raiting_______")
movie_2.raiting(25)
movie_2.show()
print("_________actors_______")
movie_1.name_actors("Nike")
movie_1.show()
