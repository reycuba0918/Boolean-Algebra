from msilib import Table
from Boolean_Constant_Expresssion import *

class thruth_table:

    def __init__(self, equation: str, output_format = int):
        self.output_format = output_format
        self.equation = equation
        self.table = {}
        
        variables_unsorted = {}
        for char in equation:
            if ord(char) >= 65 and ord(char) <= 122:
                variables_unsorted[char] = 0
        myKeys = list(variables_unsorted.keys())
        myKeys.sort()
        variables = {i: variables_unsorted[i] for i in myKeys}
        len_variables = len(variables)
        test_amount = 2**len_variables if len_variables > 0 else 0
        formatter = "0" + format(len_variables) + "b"

        for test in range(0, test_amount):
            test = format(test, formatter)
            i = 0
            for variable in variables:
                variables[variable] = test[i]
                i += 1
            test_equ = ""
            for char in equation:
                if variables.get(char):
                    test_equ += variables[char]
                else:
                    test_equ += char
            temp = boolean_constant_expresssion(test_equ)
            self.table[test] = {"equation": test_equ, "output": temp.solution}
    
    def __str__(self) -> str:
        output = ""
        if self.output_format == bool:
            for test in self.table:
                output += format("%s | %s | %r" % (test, self.table[test]["equation"], False if self.table[test]["output"] == 0 else True)) + "\n"
        else:
            for test in self.table:
                output += format("%s | %s | %d" % (test, self.table[test]["equation"], self.table[test]["output"])) + "\n"
        return output