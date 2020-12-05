# Create a collection of 6 names inputed from console ,
# generate a new collection selecting only the names starting from ‘A’ and print it
# 13. stextsel 6 hat anun parunakox havaqatsu, konsolic mutqagrvox, generacnel
# nor havaqatsu vor kparunaki miayn A-ov sksvoxnern ev tpel


name1 = []
name2 = []
# name1 = ["Ani", "Tigran", "Tina", "Areg", "Mher", "Ina"]
# print(len(name1))
count = 1
while(count < 7):
    name1.append(input("input names {}:\n".format(count)))
    count += 1
for name in name1:
    if name[0] == "A":
        name2.append(name)
print("name2 {}".format(name2))

###################
names = []
name2 = []
while(len(names) < 6):
    names.append(input("input list 2` names {}:\n".format(len(names))))
for name in names:
    if name.find('A')!=-1:
        name2.append(name)
print(name2)