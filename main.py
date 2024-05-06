from Truth_Table import truth_table
from Boolean_Constant_Expresssion import boolean_constant_expresssion
      
expression = "a * !b"

table = truth_table(expression)

print("valid: ", table.valid)
print("has_header: ", table.has_header)
print(table)

print()

table.table["01"] = boolean_constant_expresssion("1 + !1")
print("valid: ", table.valid)
print("has_header: ", table.has_header)
print(table)