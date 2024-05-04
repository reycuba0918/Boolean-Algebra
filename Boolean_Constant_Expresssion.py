class boolean_constant_expresssion:

    def __init__(self, expression: str, output_format = int) -> None:
        self.output_format = output_format
        self._expression = expression
        self._output = boolean_constant_expresssion.boolean_arithmetic(self, self._expression)
        self._valid = True

    def boolean_arithmetic(self, expression):
        arithmethic_equ = ""
        char_num = 0
        while char_num < len(expression):
            if expression[char_num] != '!':
                arithmethic_equ += expression[char_num]
            else:
                char_num += 1
                if expression[char_num] == '1':
                    arithmethic_equ += '0'
                elif expression[char_num] == '0':
                    arithmethic_equ += '1'
                elif expression[char_num] == '(':
                    brackets = ['(']
                    char_num += 1
                    inner_equ = ""
                    while len(brackets) != 0:
                        if expression[char_num] == '(':
                            brackets.append('(')
                        elif expression[char_num] == ')':
                            brackets.pop()
                            if(len(brackets) == 0):
                                break
                        inner_equ += expression[char_num]
                        char_num += 1
                    testing = self.boolean_arithmetic(inner_equ)
                    arithmethic_equ += '1' if testing == 0 else '0'
                else:
                    arithmethic_equ += expression[char_num - 1]
                    arithmethic_equ += expression[char_num]
            char_num += 1
        return eval(arithmethic_equ) if eval(arithmethic_equ) == 0 else 1

    @property
    def output(self):
        return self._output
        
    @output.setter
    def output(self, new_value):
        self._output = new_value
        self.valid = False

    @property
    def expression(self):
        return self._expression
        
    @expression.setter
    def expression(self, new_value):
        self._expression = new_value
        boolean_constant_expresssion.boolean_arithmetic(self, self._expression)
    
    @property
    def valid(self):
        return self._valid
    
    @valid.setter
    def valid(self, new_value):
        if new_value == True:
            boolean_constant_expresssion.boolean_arithmetic(self, self._expression)
            self._valid = new_value
        else:
            self._valid = new_value
    
    def __str__(self):
        if self.output_format == bool:
            return format("%s = %r" % (self._expression, False if self._output == 0 else True))
        else:
            return format("%s = %d" % (self._expression, self._output))