from Pack_task_8.inputed import numbers, count
from Pack_task_8.tarberutyun import *
from Pack_task_8.power import powers
import functools


result = functools.reduce(lambda num1, num2: num1 + num2, numbers)
print("sum is: ", result)

##############################
print("tarberutyunn =", tarberutyun(45, 39))

############################
print("power is: ", powers(5, count))