# Create 2 collections for storing movies that have been watched by 2 persons, get movies that
# are watched by at least one of them, get movies that are watched by
# 1-st and not watched by 2-nd, print results
# Создать 2 коллекции для хранения фильмов, которые смотрели 2 человека, получить фильмы,
# которые смотрел хотя бы один из них, получить фильмы, которые смотрел 1-й, а не 2-й, распечатать результаты
#####set####
people_1 = {"Dom 1", "Apokalipsis", "Avatar", "Farsazh 7", "Taxi 3"}
people_2 = {"Dom 3, 'New years", "Farsazh 7", "Taxi 3"}
print(people_1 & people_2)
print(people_1 - people_2)

###################################
people_1 = ["Dom 1", "Apokalipsis", "Avatar", "Farsazh 7", "Taxi 3"]
people_2 = ["Dom 3, 'New years", "Farsazh 7", "Taxi 3"]
group = people_2
watch_1 = []
for film in people_1:
    if film in people_2:
       print(film + " yes in both")
    else:
        group.append(film)
        watch_1.append(film)
print(watch_1)
print(group)
#########################
