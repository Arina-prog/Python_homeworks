# Input a string, print it from start to half if its length is even,
# otherwise from half to the end
# 4..Введите строку, распечатайте ее от начала до половины,
# если ее длина четная, в противном случае от половины до конца

str1 = "helow+world"
length = len(str1)
print(length)
if length % 2 == 0:
    c = int(length/2)
    print(c)
    print(str1[0:c])
else:
    c = int(length/2)
    print(str1[c:length])
