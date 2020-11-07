# Define a collection of words, input 2 new words and add them to list,
# find some inputed word in list and remove a word with some inputed index
# 8..Определите набор слов, введите 2 новых слова и добавьте их в список,
# # найдите какое-нибудь введенное слово в списке и удалите слово с некоторым введенным индексом

words = ["home", "pen", "car", "mouse", "color", "picture"]
count = 0
while(count < 2):
    words.append(input("inpur words:\n"))
    count += 1
print(words)
print(words.index("car"))
words.remove("pen")
del words[2]
print(words)