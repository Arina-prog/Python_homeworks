# Create a function with 2 parameters (function, number),
# call the function with some specific function described with lambda and integer inputed from console

num = int(input("mutqagrel tiv\n"))

def makeActions(func, num):
    print(func(num))

def summer(num):
    return num+3

makeActions(lambda num: num * 2, num)

makeActions(summer, num)
