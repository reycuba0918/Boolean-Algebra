# Bollean Algebra
This project is a Python library that offers an intuitive approach to performing Boolean arithmetic.

## Class Truth_Table
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

### `truth_table()`

`truth_table()` genarates a `truth_table` from a given `expression`.

#### Parameters for `truth_table()`

##### Required:

* `expression`: the equation from which the truth table will be generated.
  * What does this parameter accept?
    The parameter takes a boolean algebraic expression of type `str` (e.g. "A + B", "A * C)").

##### Optional:

* `output_format`: Specifies the format for displaying a `truth_table`'s outputs.
  * What does this parameter accept?
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
    * If the `output_format` is set to `bool`, in a `truth_table`, the outputs will be printed as True or False.
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

* `inputs`: This parameter establishes the keys for the `table` within its `truth_table`, where each key corresponds to a `boolean_constant_expression`. Then parameter `expression` of each `boolean_constant_expression` is formed by replacing the variables in the `truth_table`'s expression with the corresponding key.
  * What does this parameter accept?
    This parameter accepts a `list` of `str`, each consisting solely of the characters '0' or '1'. The length of each `str` must be equal to the number of variables in the `expression` of the `truth_table`.
    * By defualt this parameter holds an empty `list`. When this is the case, a `list` of all possible combinations will take it place.
      * Example:
        ```
        from Truth_Table import truth_table
      
        expression = "B * !(A + C) + A"
        
        table = truth_table(expression)
        
        print(table)
        ```
        ```
        000 | 0 * !(0 + 0) + 0 | 0
        001 | 0 * !(0 + 1) + 0 | 0
        010 | 0 * !(1 + 0) + 1 | 1
        011 | 0 * !(1 + 1) + 1 | 1
        100 | 1 * !(0 + 0) + 0 | 1
        101 | 1 * !(0 + 1) + 0 | 0
        110 | 1 * !(1 + 0) + 1 | 1
        111 | 1 * !(1 + 1) + 1 | 1
        ```
      * Example:
        ```
        from Truth_Table import truth_table
      
        expression = "B * !(A + C) + A"
        
        tests = ["000", "011"]
        
        table = truth_table(expression, inputs = tests)
        
        print(table)
        ```
        ```
        000 | 0 * !(0 + 0) + 0 | 0
        011 | 0 * !(1 + 1) + 1 | 1
        ```

### Properties for `truth_table`

* `truth_table.output_format`: hold the output format that will be used when the `truth_table` gets printed.
  * What are states that `output_format` can hold?
    * By defualt it is set to `int`. When this is the case the outputs for each outputs will etheir be a 1 or 0.
    * `bool`: when set to `bool`, if the `truth_table` prints the outputs as `True` or `False`.

* `truth_table.table`: returns an object of type `dict` that is supposed to hold all the `boolean_constant_expression`s of the `truth_table`.
  * When `truth_table.valid` is set to `True`:
    * each key in the `dict` is of type `str` and is the same size as the amount of variables that are in the `truth_table.expression`.
    * the `dict` will hold a `boolean_constant_expression` and the `expression` of each `boolean_constant_expression` will be the `truth_table`'s `expression` but with it's variables replaced by the `boolean_constant_expression`'s `dict` key.
  * When the `truth_table.table` gets modified:
    * the property `valid` is set to `False`.
    * the `truth_table`'s `inputs` get set to keys of the modified `truth_table.table`.

* `truth_table.expression`: holds the boolean algebraic expression of the `truth_table`.
  * When the `truth_table.expression` changes:
    * the `truth_table` is regenerated with the new `expression` and all possible `inputs`.
    * `truth_table.valid` is set to `True`.

* `truth_table.inputs`: This property returns a `list` of ojects of type `str` that correlates to the a `truth_table.table`'s keys.
  * When `truth_table.inputs` changes:
    * if `inputs` get set to an empty `list`, the `truth_table` will be regenerated with all possible `inputs`.
    * if `inputs` gets changed or set to a non-empty `list`, the `truth_table` will be regenerated with the new or updated `inputs`.
      * Note that the order in which the `truth_table.table` stores its items and prints them can be maniputed by the order of `inputs`.
    * `truth_table.valid` is set to `True`.

* `truth_table.valid`: is of type `bool`. It is used to determine whether `truth_table.table` has been changed manually.

The variables in `expression` are any character in the `expression` that have an ASCII value that is in between 65-122 (A-Z or a-z).

The charcters for each `input` in `inputs` replaces the variables in `expression` depending on the alphetical order of the variables in `expression`. Meaing that in `expression` "B + A", the `input` "01", would replace variable 'A' would be replaced by 0 and variable 'B' would be replaced by 1 which would be be "1 + 0". 
 
