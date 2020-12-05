# Define a string with values inside using format() method and print result
# # 9. sahmanel str vori arzheqneri mej parunakvum e format() metodn ev tpel ardyunqn

name = "Arina Saiyan"
lesson_name = "Python"
patchar = "hertapahutyan"
str1 = "es {}`s chem karox masnakcel {}`i daserin qanzi {} em \n".format(name, lesson_name, patchar)
str2 = "es {1}`i daserin chem karox masnakcel` {2} em, {0} \n ".format(name, lesson_name, patchar)
str3 = "es {0}`chem karox masnakcel {das}i dasin qanzi {patchar}ayd orn,  \n ".\
    format(name, patchar='tann chem linelu hertapahutyan em', das= 'python')
print(str1, str2, str3)