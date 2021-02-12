import itertools
import random

combinations = [combination for combination in itertools.product([0, 1], repeat=2)]
history = dict.fromkeys(combinations, 0)
print(history)

def guess_randomly():
    predicted_number = random.choice([0, 1])
    return predicted_number

def guess_shannon(prev, attempt, user_number):
    predicted_number = 0
    if attempt < 4:
        predicted_number = guess_randomly()
    else:
        if history[(prev, 0)] > history[(prev, 1)]:
            predicted_number = 0
        else:
            predicted_number = 1

    """Save history"""
    history[(prev, user_number)] += 1
    # prev = user_number
    return predicted_number


correct = 0
wrong = 0
prev = 0
attempt = 0
while True:
    user_number = int(input("input 0 or 1 \n"))
    if user_number != 1 and user_number != 0:
        continue
    predicted_number = guess_shannon(prev, attempt, user_number)
    print("user_number is ", user_number)
    print("predicted_number is", predicted_number)
    if user_number == predicted_number:
        correct += 1
        print("machine predicted correctly")
    else:
        wrong += 1
        print("machine predicted wrong")
    prev = user_number
    print("wrong is =", wrong, "\ncorrect is = ", correct, "\n")