# # voroshel personn inch dasi e patkanu txa e te axchik
#
# person = {"height": 167,
#           "weight": 60,
#           "hair color": "brown"}
#
# def predict_gender(person):
#     if person["height"]-person["weight"] <100 and person["hair color"] != "brown":
#         print("Our person is Male")
#     else:
#         print("Our person is Famale")
# predict_gender(person)
#
#
# ##############################
# # unenq mi qaniusanox amen mekn uni hachaxumneri gnahatakan ,
# # homvorqi gnahatakan , uni aktivutyan gnahatakan
# import functools
# students1 = {
#     "presents":90,
#     "homwork":80,
#     "activity":75
# }
# students2 = {
#     "presents":40,
#     "homwork":90,
#     "activity":35
# }
# students3 = {
#     "presents":70,
#     "homwork":66,
#     "activity":55
# }
# students4 = {
#     "presents":30,
#     "homwork":90,
#     "activity":65
# }
# def predict_score(student):
#     result = ((student["presents"] + student["homwork"]+student["activity"])*0.3)
#     return result
#
# print(predict_score(students1))


#############################
import random
import requests
from googlesearch import search
from bs4 import BeautifulSoup


class ChatBot:
    def reply(self, text):
        question_answers = ["maybe", "what is your opinion", "who knows"]
        simple_answers = ["it's interesting", "it's good", " are you sure?"]
        if "?" in text:
            return random.choice(question_answers)
        else:
            return random.choice(simple_answers)


class ChatBotMl:
    def reply(self, text):
        search_result_list = list(search(text, tld="com", num=10, stop=3, pause=1))
        page = requests.get(search_result_list[0])
        html_content = page.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # soup.title
        # soup.title.string
        # soup.p  # first paragraph

        # soup.find('p').text  # first paragraph text
        #
        # parent child
        # soup.p.parent.name

        ps = list(soup.find_all("p", limit=5))
        print(ps[2].text)

        # dir(soup)
        # help(soup.a)
        # print(html_content)


bob = ChatBotMl()

bob.reply("first armenian sentence")
# while True:
#     user_input = input("input your text ")
#     print(bob.reply(user_input))





