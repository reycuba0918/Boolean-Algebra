class boolean_constant_expresssion:

    def __init__(self, expression: str, output_format = int) -> None:
        self.output_format = output_format
        self.expression = expression
        self.solution = self.boolean_arithmetic(expression)

    def __str__(self):
        if self.output_format == bool:
            return format("%s = %r" % (self.expression, False if self.solution == 0 else True))
        else:
            return format("%s = %d" % (self.expression, self.solution))

    def boolean_arithmetic(self, equ: str) -> int:
        arithmethic_equ = ""
        char_num = 0
        while char_num < len(equ):
            if equ[char_num] == '!':
                char_num += 1
                if equ[char_num] == '1':
                    arithmethic_equ += '0'
                elif equ[char_num] == '0':
                    arithmethic_equ += '1'
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
                    arithmethic_equ += "1" if self.boolean_arithmetic(inner_equ) == 0 else "0"
                else:
                    arithmethic_equ += equ[char_num - 1]
                    arithmethic_equ += equ[char_num]
            else:
                arithmethic_equ += equ[char_num]
            char_num += 1
        return eval(arithmethic_equ) if eval(arithmethic_equ) == 0 else 1