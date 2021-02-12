import itertools
import random

combinations = [combination for combination in itertools.product([0, 1, 2], repeat=2)]
history = dict.fromkeys(combinations, 0)
print(history)


def guess_randomly():
    predicted_number = random.choice([0, 1, 2])
    return predicted_number


print(guess_randomly())


def guess_shannon(prev, attempt, user_number):
    predicted_number = 0
    if attempt < 4:
        predicted_number = guess_randomly()
    else:
        if history[(prev, 0)] > history[(prev, 1)] > history[(prev, 2)]:
            predicted_number = 1
        elif history[(prev, 0)] < history[(prev, 1)] < history[(prev, 2)]:
            predicted_number = 0
        else:
            predicted_number = 2

    """Save history"""
    history[(prev, user_number)] += 1
    return predicted_number


victory = 0
beating = 0
prev = 0
attempt = 0
while True:
    user_number = int(input("input 0 is stone, 1 is paper  or 2 is scissors\n"))
    if user_number != 1 and user_number != 0 and user_number != 2:
        continue
    predicted_number = guess_shannon(prev, attempt, user_number)
    print("user_number is ", user_number)
    print("predicted_number is", predicted_number)
    if user_number == predicted_number:

        print(victory, beating)
    elif (user_number == 0 and predicted_number == 2) or (user_number == 1 and predicted_number == 0) or \
            (user_number == 2 and predicted_number == 1):
        beating += 1
        print("machine predicted wrong")
    else:
        victory += 1
        prev = user_number
    print("beating is =", beating, "\nvictory is = ", victory, "\n")


