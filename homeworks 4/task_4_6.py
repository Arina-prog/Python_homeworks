# Define a collection of programming languages (names), add new language name from console if it’s not C#
# 6.. Определите набор языков программирования (имена),
# # добавьте новое имя языка из консоли, если это не C #

langug = ["c++", "java", "python", "pascal", "js"]
new =input("input programming languages:\n")
if new != "c#":
    langug.append(new)
    print(langug)
else:
    print("inpuded is c#")