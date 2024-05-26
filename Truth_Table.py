from Boolean_Constant_Expresssion import *
from util.My_Dictionary import *
from util.My_List import *

class truth_table:
    
    def __init__(self, expression: str, output_format: type = int, has_header: bool = True, inputs: list[str] = []):

        self._output_format = output_format
        self._has_header = has_header
        self._table = my_dictionary(self)
        self._expression = expression
        self._inputs = my_list(self, inputs)

        truth_table.make_table(self)
   
    def make_table(self):
        self._table.initialing = True
        keys = set()
        for character in self._expression:
            int_character = ord(character)
            if int_character >= 65 and int_character <= 122:
                keys.add(character)

        variables = {}
        len_variables = len(keys)
        if not self._inputs:
            amount_of_tests = 2**len_variables if len_variables > 0 else 0
            formatter = "0" + format(len_variables) + "b"
            for input in range(0, amount_of_tests):
                input = format(input, formatter)
                i = 0
                for key in sorted(keys):
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
                    for key in sorted(keys):
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
        self._table.valid = True

    def update_inputs(self):
        self._inputs = my_list(self, self.table.keys())

    def reset_inputs(self):
        self._inputs.clear()
    
    @property
    def has_header(self):
        return self._has_header
    
    @has_header.setter
    def has_header(self, new_value):
        self._has_header = new_value
    
    @property
    def output_format(self):
        return self._output_format
    
    @output_format.setter
    def output_format(self, new_value):
        self._output_format = new_value

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
        return list(self._inputs)
        
    @inputs.setter
    def inputs(self, new_value):
        self._inputs = my_list(self, new_value)
        self.make_table()
    
    @property
    def valid(self):
        return self._table.valid
    
    @valid.setter
    def valid(self, new_value):
        if new_value == True:
            self.make_table()

    def __str__(self) -> str:
        output = ""
        if self._inputs == {}:
            return output
        my_space = ''
        in_formatter = "%s"
        if self._has_header and self.valid:
            my_space = ' '
            input_i = self._inputs[0]
            len_in = len(input_i) if len(input_i) >= 2 else 2
            in_formatter = "%-" + format(len_in) + 's'
            output += my_space + format(in_formatter % "in") + ' | '
            len_expression = len(self._table[input_i].expression)
            expression_formatter = "%-" + format(len_expression) + 's'
            output += format(expression_formatter % self._expression) + ' | '
            output += "out\n"
            for i in range(0, len_in + 2):
                output += '-'
            output += '|'
            for i in range(0, len_expression + 2):
                output += '-'
            output += '|-----\n'
        for i in range(0, len(self._inputs)):
            input_i = self._inputs[i]
            if self.output_format == bool:
                output_formatter = "%s" + in_formatter + " | %s | %r"
                if i < len(self._inputs) - 1:
                    output += format( output_formatter % (my_space, input_i, self._table[input_i].expression, False if self._table[input_i].output == 0 else True)) + "\n"
                else:
                    output += format(output_formatter % (my_space, input_i, self._table[input_i].expression, False if self._table[input_i].output == 0 else True))  
            else:
                output_formatter = "%s" + in_formatter + " | %s | %s%d"
                if i < len(self._inputs) - 1:
                    output += format(output_formatter % (my_space, input_i, self._table[input_i].expression, my_space, self._table[input_i].output)) + "\n"
                else:
                    output += format(output_formatter % (my_space, input_i, self._table[input_i].expression, my_space, self._table[input_i].output))
        return output
    
    def sub_table(self, inputs: list[str] = []):
        if not inputs:
            return truth_table(self._expression, self.output_format, self._has_header, self.inputs)
        else:
            return truth_table(self._expression, self.output_format, self._has_header, inputs)
