class boolean_expresssion:
    
    def __init__(self, Expression: str) -> None:
        self.solution = self.boolean_arithmetic(Expression)

    def __str__(self) -> str:
        self.solution

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
                    arithmethic_equ += format(self.boolean_arithmetic(inner_equ))
                else:
                    arithmethic_equ += equ[char_num]
            else:
                arithmethic_equ += equ[char_num]
            char_num += 1
        solution = eval(arithmethic_equ)
        return 1 if solution > 0 else 0