# Bollean Algebra
This project is a Python library that offers an intuitive approach to performing Boolean arithmetic.

## Class Truth_Table
This class creates truth tables for a boolean algebraic expression.

### Big Idea

code:
```
from Truth_Table import truth_table

table = truth_table("A + !(B * C)")

print(table)
```
Output:
```
 in  | A + !(B * C) | out
-----|--------------|-----
 000 | 0 + !(0 * 0) |  1
 001 | 1 + !(0 * 0) |  1
 010 | 0 + !(0 * 1) |  1
 011 | 1 + !(0 * 1) |  1
 100 | 0 + !(1 * 0) |  1
 101 | 1 + !(1 * 0) |  1
 110 | 0 + !(1 * 1) |  0
 111 | 1 + !(1 * 1) |  1
```

### `truth_table()`

`truth_table()` genarates a `truth_table` from a given `expression`.

#### Parameters for `truth_table()`

##### Required:

* `expression`: intakes the boolean algebraic expression of type `str` from which the truth table will be generated which will be stored in the property `expression`. 
  * e.g. "A + B", "A * C"

##### Optional:

* `output_format`: this parameter intiates property `output_format` which specifies the format for displaying a `truth_table`'s outputs.
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
         in  | A + !(B * C) | out
        -----|--------------|-----
         000 | 0 + !(0 * 0) |  1
         001 | 1 + !(0 * 0) |  1
         010 | 0 + !(0 * 1) |  1
         011 | 1 + !(0 * 1) |  1
         100 | 0 + !(1 * 0) |  1
         101 | 1 + !(1 * 0) |  1
         110 | 0 + !(1 * 1) |  0
         111 | 1 + !(1 * 1) |  1
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
         in  | A + !(B * C) | out
        -----|--------------|-----
         000 | 0 + !(0 * 0) | True
         001 | 0 + !(1 * 0) | True
         010 | 1 + !(0 * 0) | True
         011 | 1 + !(1 * 0) | True
         100 | 0 + !(0 * 1) | True
         101 | 0 + !(1 * 1) | False
         110 | 1 + !(0 * 1) | True
         111 | 1 + !(1 * 1) | True
        ```

* `inputs`: This parameter establishes the keys for the property `table` within its `truth_table`, where each key corresponds to a `boolean_constant_expression`. Note that the parameter `expression` of each `boolean_constant_expression` is formed by replacing the variables in `truth_table`'s `expression`, with the corresponding key.
  * Note that this parameter initiates the property `inputs`. 
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
         in  | B * !(A + C) + A | out
        -----|------------------|-----
         000 | 0 * !(0 + 0) + 0 |  0
         001 | 0 * !(0 + 1) + 0 |  0
         010 | 0 * !(1 + 0) + 1 |  1
         011 | 0 * !(1 + 1) + 1 |  1
         100 | 1 * !(0 + 0) + 0 |  1
         101 | 1 * !(0 + 1) + 0 |  0
         110 | 1 * !(1 + 0) + 1 |  1
         111 | 1 * !(1 + 1) + 1 |  1
        ```
    * When a `list` is provided the the keys of `truth_table.table` are going to match the `list`. Note that this includes the order, meaing that the `truth_table` will print in order of the `list`.
      * Example:
        ```
        from Truth_Table import truth_table
      
        expression = "B * !(A + C) + A"
        
        tests = ["011", "000", "100", "100"]
        
        table = truth_table(expression, inputs = tests)
        
        print(table)
        ```
        ```
         in  | B * !(A + C) + A | out
        -----|------------------|-----
         011 | 1 * !(0 + 1) + 0 |  0
         000 | 0 * !(0 + 0) + 0 |  0
         100 | 0 * !(1 + 0) + 1 |  1
         100 | 0 * !(1 + 0) + 1 |  1
        ```

### Properties for `truth_table`

* `truth_table.output_format`: hold the output format that will be used when the `truth_table` gets printed.
  * What are states that `output_format` can hold?
    * By defualt it is set to `int`. When this is the case the outputs for each outputs will etheir be a '1' or '0'.
      * Example:
        ```
        from Truth_Table import truth_table
        
        expression = "(a * b)"
        
        table = truth_table(expression)
        
        print(table)
        ```
        ```
         in | (a * b) | out
        ----|---------|-----
         00 | (0 * 0) |  0
         01 | (0 * 1) |  0
         10 | (1 * 0) |  0
         11 | (1 * 1) |  1
        ```
    * `bool`: when set to `bool`, the outputs printed by the `truth_table` will appear as True or False.
      * Example:
        ```
        from Truth_Table import truth_table
        
        expression = "(a * b)"
        
        table = truth_table(expression)
        
        table.output_format = bool
        
        print(table)
        ```
        ```
         in | (a * b) | out
        ----|---------|-----
         00 | (0 * 0) | False
         01 | (1 * 0) | False
         10 | (0 * 1) | False
         11 | (1 * 1) | True
        ```
      
* `truth_table.table`: returns an object of type `dict` that is supposed to hold all the `boolean_constant_expression`s of the `truth_table`.
  * When `truth_table.valid` is set to `True`:
    * each key in the `dict` is of type `str` and is the same size as the amount of variables that are in the `truth_table.expression`.
    * the `dict` will hold `boolean_constant_expression`s, where the `expression` of each `boolean_constant_expression` will be the `truth_table`'s `expression` but with it's variables being replaced by the `boolean_constant_expression` `truth_table.table`'s key.
  * When the `truth_table.table` gets modified:
    * the property `valid` is set to `False`.
    * the `truth_table`'s `inputs` get set to the keys of the modified `truth_table.table`.

* `truth_table.expression`: holds the boolean algebraic expression of the `truth_table`.
  * When the `truth_table.expression` changes:
    * the `truth_table` is regenerated with the new `expression` and all possible `inputs`.
      * Example:
        ```
        from Truth_Table import truth_table

        expression = "(a * b)"
        
        tests = ["01", "11"]
        
        table = truth_table(expression, inputs = tests)
        
        print(table)
        
        print()
        
        table.expression = "C * !(A + B)"
        
        print(table)
        ```
        ```
         in | (a * b) | out
        ----|---------|-----
         01 | (1 * 0) |  0
         11 | (1 * 1) |  1
        
         in  | C * !(A + B) | out
        -----|--------------|-----
         000 | 0 * !(0 + 0) |  0
         001 | 0 * !(1 + 0) |  0
         010 | 1 * !(0 + 0) |  1
         011 | 1 * !(1 + 0) |  0
         100 | 0 * !(0 + 1) |  0
         101 | 0 * !(1 + 1) |  0
         110 | 1 * !(0 + 1) |  0
         111 | 1 * !(1 + 1) |  0
        ```
    * `truth_table.valid` is set to `True`.

* `truth_table.inputs`: This property returns a `list` of ojects of type `str` that correlates to the a `truth_table.table`'s keys.
  * When `truth_table.inputs` changes:
    * if `inputs` get set to an empty `list`, the `truth_table` will be regenerated with all possible `inputs`.
      * Example:
        ```
        from Truth_Table import truth_table

        expression = "A + B * C"
        
        tests = ["000", "010", "100"]
        
        table = truth_table(expression, inputs = tests)
        
        print(table)
        
        print()
        
        table.inputs.clear()
        
        print(table)
        ```
        ```
         in  | A + B * C | out
        -----|-----------|-----
         000 | 0 + 0 * 0 |  0
         010 | 0 + 1 * 0 |  0
         100 | 0 + 0 * 1 |  0
        
         in  | A + B * C | out
        -----|-----------|-----
         000 | 0 + 0 * 0 |  0
         001 | 1 + 0 * 0 |  1
         010 | 0 + 1 * 0 |  0
         011 | 1 + 1 * 0 |  1
         100 | 0 + 0 * 1 |  0
         101 | 1 + 0 * 1 |  1
         110 | 0 + 1 * 1 |  1
         111 | 1 + 1 * 1 |  1
         ```
    * if `inputs` gets changed or set to a non-empty `list`, the `truth_table` will be regenerated with the new or updated `inputs`.
      * Note that the order in which the `truth_table.table` stores its items and prints them can be maniputed by the order of `inputs`.
        * Example:
          ```
          from Truth_Table import truth_table

          expression = "A + B * C"
          
          table = truth_table(expression)
          
          print(table)
          
          print()
          
          table.inputs = tests = ["000", "010", "000", "011", "011"]
          
          print(table)
          ```
          ```
           in  | A + B * C | out
          -----|-----------|-----
           000 | 0 + 0 * 0 |  0
           001 | 0 + 1 * 0 |  0
           010 | 1 + 0 * 0 |  1
           011 | 1 + 1 * 0 |  1
           100 | 0 + 0 * 1 |  0
           101 | 0 + 1 * 1 |  1
           110 | 1 + 0 * 1 |  1
           111 | 1 + 1 * 1 |  1
          
           in  | A + B * C | out
          -----|-----------|-----
           000 | 0 + 0 * 0 |  0
           010 | 1 + 0 * 0 |  1
           000 | 0 + 0 * 0 |  0
           011 | 1 + 1 * 0 |  1
           011 | 1 + 1 * 0 |  1
          ```
    * `truth_table.valid` is set to `True`.

* `truth_table.valid`: is of type `bool`. It is used to determine whether `truth_table.table` has been changed manually.

The variables in `expression` are any character in the `expression` that have an ASCII value that is in between 65-122 (A-Z or a-z).

The charcters for each `input` in `inputs` replaces the variables in `expression` depending on the alphetical order of the variables in `expression`. Meaing that in `expression` "B + A", the `input` "01", would replace variable 'A' would be replaced by 0 and variable 'B' would be replaced by 1 which would be be "1 + 0". 
 
