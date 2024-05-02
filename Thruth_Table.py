from Boolean_Expresssion import boolean_expresssion

class thruth_table:
    def __init__(self, Equation: str) -> None:
        variables_unsorted = {}
        for char in Equation:
            if ord(char) >= 65 and ord(char) <= 122:
                variables_unsorted[char] = 0
        myKeys = list(variables_unsorted.keys())
        myKeys.sort()
        variables = {i: variables_unsorted[i] for i in myKeys}

        len_variables = len(variables)

        test_amount = 2**len_variables if len_variables > 0 else 0

        formatter = "0" + format(len_variables) + "b"

        self.tests = {}
        for test in range(0, test_amount):

            test = format(test, formatter)

            i = 0
            for variable in variables:
                variables[variable] = test[i]
                i += 1

            test_equ = ""
            for char in Equation:
                if variables.get(char):
                    test_equ += variables[char]
                else:
                    test_equ += char
            temp = boolean_expresssion(test_equ)
            self.tests[test] = (format("%s | %s | %d" % (test, test_equ, temp.solution)))
    
    def __str__(self) -> str:
        output = ""
        for test in self.tests:
            output += self.tests[test] + "\n"
        return output