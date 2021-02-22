import random


class ChatBot:

    def reply(self, text):
        question_answers = ["hianali", "shnorhakalutyun esel em lav", "inchov es zbaxvats?", "cankanu em zbosnel",
                            "mets uraxutyamb", "anshusht", "kzangem, by"]
        simple_answers = ["es lav em du inchpes es?", "hianali isk du?", "es nuynpes", "kmianas indz?",
                          "kspasem zangit, by"]
        bot_start = ["Voxjuyn inchpes es?", "Barev", "barev ek shbvenq?", "barev inchpes es?"]
        goodby = ["by", "goodby"]
        if text == "start":
            return random.choice(bot_start)
        if text == "by" or text == "by?":
            return random.choice(goodby)

        if "?" in text:
            return random.choice(question_answers)
        else:
            return random.choice(simple_answers)


Bob = ChatBot()
Jek = ChatBot()


while True:
    user_input = input("mutq start  ")
    if user_input != "start":
        continue

    while True:

        if "by" in user_input:
            break
        else:
            Bobs = Bob.reply(user_input)
            print("Bob typing ...\n", "  ", Bobs)
        if "by" in Bobs:
            break
        else:
            Jeks = Jek.reply(Bobs)
            print("Jek tayping ...\n", "  ", Jeks)
        user_input = Jeks
