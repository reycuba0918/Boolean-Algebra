# Bollean Algebra
This project is a Python library that offers an intuitive approach to performing Boolean arithmetic.

## `truth_table()`
This class creates truth tables for a boolean algebraic expression.

### Big Idea
code:
```
from Truth_Table import truth_table

print(truth_table("A + !(B * C)"))
```
Output:
```
000 | 0 + !(0 * 0) | 1
001 | 0 + !(0 * 1) | 1
010 | 0 + !(1 * 0) | 1
011 | 0 + !(1 * 1) | 0
100 | 1 + !(0 * 0) | 1
101 | 1 + !(0 * 1) | 1
110 | 1 + !(1 * 0) | 1
111 | 1 + !(1 * 1) | 1
```
### Parameters for `truth_table()`
* Required:
  * `expression`: the equation from which the truth table will be generated. The parameter is a boolean algebraic expression of type `str` (e.g. "A + B", "A * C)").
* optional:
  * `output_format`: Specifies the format for displaying a truth_table's outputs. The available states for this parameter are listed below.
    * By defualt `output_format` is set to `int` meaning that the outputs will etheir be a 1 or 0.
      * Example:
        ```
        from Truth_Table import truth_table

        expression = "A + !(B * C)"
        table = truth_table(expression)
        print(table)
        ```
        ```
        000 | 0 + !(0 * 0) | 1
        001 | 0 + !(0 * 1) | 1
        010 | 0 + !(1 * 0) | 1
        011 | 0 + !(1 * 1) | 0
        100 | 1 + !(0 * 0) | 1
        101 | 1 + !(0 * 1) | 1
        110 | 1 + !(1 * 0) | 1
        111 | 1 + !(1 * 1) | 1
        ```
    * If the `output_format` is set to `bool`, in a truth_table, the outputs will be printed as True or False.
      * Example:
        ```
        from Truth_Table import truth_table

        expression = "A + !(B * C)"
        table = truth_table(expression, output_format = bool)
        print(table)
        ```
        ```
        000 | 0 + !(0 * 0) | True
        001 | 0 + !(0 * 1) | True
        010 | 0 + !(1 * 0) | True
        011 | 0 + !(1 * 1) | False
        100 | 1 + !(0 * 0) | True
        101 | 1 + !(0 * 1) | True
        110 | 1 + !(1 * 0) | True
        111 | 1 + !(1 * 1) | True
        ```
  * `inputs`: spesifies the keys for it's truth_table's table that holds boolean_constant_expresssions whos `expression`s are the truth_table's `expression` with the key replacing the varables. This parameter accepts a list of `str` objects that are only made up of the charcters '0' or '1' and that have a size that is equvelant to amount of variables in its truth_table's `expression`.


 Variables in a boolean algebraic `expression`

 The variables in `expression` are any character in the `expression` that have an ASCII value that is in between 65-122 (A-Z or a-z).
 The charcters for each `input` in `inputs` replaces the variables in `expression` depending on the alphetical order of the variables in `expression`. Meaing that in `expression` "B + A", the `input` "01", would replace variable 'A' would be replaced by 0 and variable 'B' would be replaced by 1 which would be be "1 + 0". 
 
