import random
import requests
from googlesearch import search
from bs4 import BeautifulSoup

class ChatBot:

    def reply(self, text):
        simple_answers = ["Who created the Armenian alphabet?", "where Mesrop Mashtots was born?"]
        if "?" in text:
            return random.choice(simple_answers)
        else:
            return random.choice(simple_answers)

#
# bob = ChatBot()
#
# jek = ChatBot()
# answer = ""
#
# while True:
#     if "by" in answer:
#         break
#     else:
#         answer = bob.reply(answer)
#         print("Bob typing ...\n", "  ", answer)
#     if "by" in answer:
#         break
#     else:
#         answer = jek.reply(answer)
#         print("Jek tayping ...\n", "  ", answer)



class ChatBotMl:
    def reply(self, text):
        search_result_list = list(search(text, tld="com", num=10, stop=3, pause=1))
        page = requests.get(search_result_list[0])
        html_content = page.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # soup.title
        # soup.title.string
        # soup.p  # first paragraph
        #
        # soup.find('p').text  # first paragraph text
        # parent child
        # soup.p.parent.name

        ps = list(soup.find_all("p", limit=5))
        print(ps[2].text)

        # dir(soup)
        # help(soup.a)
        # print(html_content)


bob = ChatBotMl()
jek = ChatBotMl()

answer = "hello"
while True:
    answer = jek.reply(answer)
    # print(answer)
    answer = bob.reply(answer)
    # print(answer)