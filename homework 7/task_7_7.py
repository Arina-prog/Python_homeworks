# Create several functions store them inside variables for handling collection of
# movie names using lambdas

# Создайте несколько функций,
# сохраните их внутри переменных для обработки коллекции имен фильмов с
# использованием лямбда-выражений


movies = ["Farsazh 1", "Farsazh 2", "Farsazh 3", "Farsazh 4"]
movies1 = ["Dom 1", "Golodnye igri", "Apocalipsis", "Farsazh 4"]
is_the = lambda name: name.lower()[:3] == "Far"
movie_name = list(filter(is_the, movies))
print(movie_name)
