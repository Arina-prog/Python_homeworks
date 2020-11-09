# Define collection of prices, calculate their sum until meeting negative price
# Определите совокупность цен, рассчитайте их сумму до достижения отрицательной цены

price = [25600, 1450, -2560, 1500]
sum = 0
for pr in price:
    if pr > 0:
        sum += pr
    else:
        break
print(sum)


