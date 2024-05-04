from Boolean_Constant_Expresssion import *
from My_Dictionary import *
from My_List import *

class truth_table:
    
    def __init__(self, expression: str, output_format: type = int, inputs: list[str] = []):

        self._output_format = output_format
        self._table = my_dictionary(self)
        self._expression = expression
        self._inputs = my_list(self, inputs)

        truth_table.make_table(self)
   
    def make_table(self):
        self._table.initialing = True
        self.table.valid = True
        keys = []
        for character in self._expression:
            int_character = ord(character)
            if int_character >= 65 and int_character <= 122:
                keys += character
        keys.sort()

        variables = {}
        len_variables = len(keys)
        if not self._inputs:
            amount_of_tests = 2**len_variables if len_variables > 0 else 0
            formatter = "0" + format(len_variables) + "b"
            for input in range(0, amount_of_tests):
                input = format(input, formatter)
                i = 0
                for key in keys:
                    variables[key] = input[i]
                    i += 1
                test_equation = ""
                for character in self._expression:
                    if character in variables:
                        test_equation += variables[character]
                    else:
                        test_equation += character
                self._table[input] = boolean_constant_expresssion(test_equation)
                self._inputs += [input]
        else:
            for input in self._inputs:
                if len(input) == len_variables:
                    i = 0
                    for key in keys:
                        testing = input[i]
                        if testing == '0' or testing == '1':
                            variables[key] = input[i]
                        else:
                            raise ValueError()
                        i += 1
                    test_equation = ""
                    for character in self._expression:
                        if character in variables:
                           test_equation += variables[character]
                        else:
                            test_equation += character 
                else:
                    raise ValueError()
                self._table[input] = boolean_constant_expresssion(test_equation)
        self._table.initialing = False

    def update_inputs(self):
        self._inputs = list(self._table.keys())

    def reset_inputs(self):
        self._inputs.clear()
    
    @property
    def output_format(self):
        return self._output_format
    
    @output_format.setter
    def output_format(self, new_value):
        self.output_format = new_value

    @property
    def table(self):
        return self._table
    
    @table.setter
    def table(self, new_value):
        self._table = my_dictionary(self, new_value)
        self._table.valid = False
        self.update_inputs()
    
    @property
    def expression(self):
        return self._expression
        
    @expression.setter
    def expression(self, new_value):
        self._expression = new_value
        self.reset_inputs()
        self.make_table()

    @property
    def inputs(self):
        return self._inputs
        
    @inputs.setter
    def inputs(self, new_value):
        self._inputs = my_list(self, new_value)
        self.make_table()
    
    @property
    def valid(self):
        return self.table.valid
    
    @valid.setter
    def valid(self, new_value):
        if new_value == True:
            self.make_table()

    def __str__(self) -> str:
        out = ""
        for test in self._inputs:
            if self.output_format == bool:
                out += format("%s | %s | %r" % (test, self._table[test].expression, False if self._table[test].output == 0 else True)) + "\n"
            else:
                out += format("%s | %s | %d" % (test, self._table[test].expression, self._table[test].output)) + "\n"
        return out
    
    def sub_table(self, inputs: list[str] = []):
        if not inputs:
            return truth_table(self._expression, self.output_format, self.inputs)
        else:
            return truth_table(self._expression, self.output_format, inputs)
