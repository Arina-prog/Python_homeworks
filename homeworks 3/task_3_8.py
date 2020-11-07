# Create 2 modules: 1. stores some attributes about a room
# (color, number, etc.); 2. makes some operations on attributes of first module
# 8...stextsel 2 modul 1-@ parunakum e senyaki masin info guyn hamar ev ayln 2-@ katarum e gortsoxutyun dranc het

import room_params

if (room_params.color == "red"):
    room_params.color = "blue"
    print(room_params.color)
elif (room_params.floor == 5):
    room_params.color = "yellow"
else:
    room_params.color = "black"
    room_params.floor = 3
    print(room_params.color)
    print(room_params.floor)
