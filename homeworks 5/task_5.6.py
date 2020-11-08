# *Input string of words separated by coma, get number of words and print it
# 6.. Введите строку слов, разделенных запятой, получите количество слов и распечатайте его

str1 = input("Input string of words separated by coma:\n")
word_count = 0
for char in str1:
    if char == ",":
        word_count += 1
print(word_count+1)
