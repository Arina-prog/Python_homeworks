# *Input string of words separated by coma, get number of words and print it
# 6.. Введите строку слов, разделенных запятой, получите количество слов и распечатайте его

str_2 = input('Input string 2 \n: ')
number_of_words = str_2.count(',') + 1
print(number_of_words)

#####################

str1 = input("Input string 1 of words separated by coma:\n")
word_count = 0
for char in str1:
    if char == ",":
        word_count += 1
print(word_count+1)



