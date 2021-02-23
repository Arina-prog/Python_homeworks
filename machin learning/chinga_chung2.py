import itertools
import random

combinations = [combination for combination in itertools.product(["stone", "paper", "scissors"], repeat=2)]
history = dict.fromkeys(combinations, 0)
print(history)


def guess_randomly():
    predicted_number = random.choice(["stone", "paper", "scissors"])
    return predicted_number


print(guess_randomly())


def guess_shannon(prev, attempt, user_input):
    predicted_number = "stone"
    if attempt < 4:
        predicted_number = guess_randomly()
    else:
        if history[(prev, "stone")] > history[(prev, "paper")] > history[(prev, "scissors")]:
            predicted_number = predicted_number
        elif history[(prev, "stone")] < history[(prev, "paper")] < history[(prev, "scissors")]:
            predicted_number = "stone"
        else:
            predicted_number = "scissors"

    """Save history"""
    history[(prev, user_input)] += 1
    return predicted_number


machin_account = 0
user_account = 0
prev = "stone"
attempt = 0
while True:
    user_input = input("input  'stone', or 'paper'  or 'scissors'\n")
    if user_input != "paper" and user_input != "stone" and user_input != "scissors":
        continue
    predicted_number = guess_shannon(prev, attempt, user_input)
    print("user_number is ...", user_input)
    print("predicted_number is...", predicted_number)
    if user_input == predicted_number:
        print("account is \n machin ={}, user = {}".format(machin_account, user_account))
    elif (user_input == "stone" and predicted_number == "scissors") or\
            (user_input == "paper" and predicted_number == "stone") or \
            (user_input == "scissors" and predicted_number == "paper"):
        user_account += 1
        print("machine predicted wrong")
    else:
        machin_account += 1
        prev = user_input
    print("machin account =", machin_account, "\n user_account = ", user_account, "\n")
