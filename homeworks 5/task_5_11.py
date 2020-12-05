# Create a regular expression to find occurences of regular expression in strings
# *Define a collection of numbers, generate a new collection selecting
# only odd or dividable by 6 numbers and print it
#11.stextsel kanonavor artahaytutyun, gtnel depqern str-i mej exats kanonavor artahaytutyunneern

str2 = " es unem %d txa, na %s tarekan e nra anunn %s e"
str_2= str2 % (1, 2.5, "Alex")
print(str2.count('%'))

####################

str1 = " es unem %d txa, na %s tarekan e nra anunn %s e"
str_1 = str1 % (1, 2.5, "Alex")
print(str_1)
count = 0
for i in str1:
    if i == "%":
        count += 1
print(count)


