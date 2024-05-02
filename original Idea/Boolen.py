def boolean_arithmetic(equ: str):
    solution = ""
    char_num = 0
    while char_num < len(equ):
        if equ[char_num] == '!':
            char_num += 1
            if equ[char_num] == '1':
                solution += '0'
            elif equ[char_num] == '0':
                solution += '1'
            elif equ[char_num] == '(':
                brackets = ["("]
                char_num += 1
                inner_equ = ""
                while len(brackets) != 0:
                    if equ[char_num] == '(':
                        brackets.append('(')
                    elif equ[char_num] == ')':
                        brackets.pop()
                        if(len(brackets) == 0):
                            break
                    inner_equ += equ[char_num]
                    char_num += 1
                solution += format(boolean_arithmetic(inner_equ))
            else:
                solution += equ[char_num]
        else:
            solution += equ[char_num]
        char_num += 1
    return eval(solution) if eval(solution) == 0 else 1

def solve_boolean_expression(equ: str):
    variables_unsorted = {}
    for char in equ:
        if ord(char) >= 65 and ord(char) <= 122:
            variables_unsorted[char] = 0
    myKeys = list(variables_unsorted.keys())
    myKeys.sort()
    variables = {i: variables_unsorted[i] for i in myKeys}

    len_variables = len(variables)

    test_amount = 2**len_variables if len_variables > 0 else 0

    formatter = "0" + format(len_variables) + "b"

    tests = {}
    for test in range(0, test_amount):

        test = format(test, formatter)

        i = 0
        for variable in variables:
            variables[variable] = test[i]
            i += 1

        test_equ = ""
        for char in equ:
            if variables.get(char):
                test_equ += variables[char]
            else:
                test_equ += char
        
        tests[test] = (format("%s | %s | %d" % (test, test_equ, boolean_arithmetic(test_equ))))
    return tests

def printTruthTable(order, equ_tests):
    for test in order:
        print(equ_tests[test])

equ = "A * !C * (!B + B)"
tests = solve_boolean_expression(equ)
order = ['000', '100', '001', '101', '010', '110']

printTruthTable(order, tests)