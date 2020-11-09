# *Define a game board (2x2 matrix) with 2 bomb values and
# 2 gold values, provide user 3 attempts to find all gold values
#9... Определите игровое поле (матрица 2x2) с 2 значениями бомбы
# и 2 значениями золота, предоставьте пользователю 3 попытки найти все значения золота
count = 0
game = [["bomb", "gold"], ["gold", "bomb"]]
while(count < 3):
    user = int(input("input  1, 2, 3 or 4:\n"))
    if user == 1:
        print(game[0][0])
    if user == 2:
        print(game[0][1])
    if user == 3:
        print(game[1][0])
    if user == 4:
        print(game[1][1])
    count += 1

