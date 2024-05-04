from Truth_Table import *
from Boolean_Constant_Expresssion import *


test = truth_table("A + B * !(C + D)", inputs=["0000", "0011"])
print(test)

test.inputs = ["0000", "1100"]

print(test)