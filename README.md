# Bollean Algebra
This project is a Python library that offers an intuitive approach to performing Boolean arithmetic.

## Class Boolean_Constant_Expresssion

This class creates a way to store and solve boolean expressions that are only made up of the constants'0' or '1'.

### Big Idea

Code:
```
from Boolean_Constant_Expresssion import boolean_constant_expresssion

expression = boolean_constant_expresssion("1 * 0 + 1")

print(expression)
```
Output:
```
1 * 0 + 1 = 1
```
### `boolean_constant_expresssion()`

`boolean_constant_expresssion()` creates a `boolean_constant_expresssion` from a given `expression`.

#### `boolean_constant_expresssion()` parameters:

##### Required:

* `expression`: fills the property `boolean_constant_expresssion.expression`.

##### Optional:

* `output_format`: 

#### `boolean_constant_expresssion()` properties:

* `expression`: holds the boolean constant expression of a `boolean_constant_expression`.

* `output`: holds the boolean answer for the `expression` in its `boolean_constant_expresssion`.

* `valid`: states whether `output` has been changed manually.

* `output_format`: determines the format of the answer when it's `boolean_constant_expresssion` is printed.

## Class Truth_Table

This class creates truth tables for a boolean algebraic expression.

### Big Idea

Code:
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

* `has_header`: this parameter passes its value to the property `has_header`, which determines whether a `valid` `truth_table` gets printed with its header.
  * By default it is set to `True`. So a default `valid` `truth_table` would print with it's header. 
    * Example:
      ```
      from Truth_Table import truth_table

      expression = "a * !b"
      
      table = truth_table(expression)
      
      print(table)
      ```
      ```
       in | a * !b | out
      ----|--------|-----
       00 | 0 * !0 |  0
       01 | 1 * !0 |  1
       10 | 0 * !1 |  0
       11 | 1 * !1 |  0
      ```
  * When `has_header` is False, the `truth_table` would be printed without a header.
    * Example:
      ```
      from Truth_Table import truth_table
      
      expression = "a * !b"
      
      table = truth_table(expression, has_header = False)
      
      print(table)
      ```
      ```
      00 | 0 * !0 | 0
      01 | 1 * !0 | 1
      10 | 0 * !1 | 0
      11 | 1 * !1 | 0
      ```
  * Note that when the `truth_table` is not `valid` the `truth_table` will print without header even if `has_header` has been set to `True`.
    * For example:
      ```
      from Truth_Table import truth_table
      from Boolean_Constant_Expresssion import boolean_constant_expresssion
            
      expression = "a * !b"
      
      table = truth_table(expression)
      
      print("valid: ", table.valid)
      print("has_header: ", table.has_header)
      print(table)
      
      print()
      
      table.table["01"] = boolean_constant_expresssion("1 + !1")
      print("valid: ", table.valid)
      print("has_header: ", table.has_header)
      print(table)
      ```
      ```
      valid:  True
      has_header:  True
       in | a * !b | out
      ----|--------|-----
       00 | 0 * !0 |  0
       01 | 0 * !1 |  0
       10 | 1 * !0 |  1
       11 | 1 * !1 |  0
      
      valid:  False
      has_header:  True
      00 | 0 * !0 | 0
      01 | 1 + !1 | 1
      10 | 1 * !0 | 1
      11 | 1 * !1 | 0
      ```

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

* `inputs`: This parameter initiates the property `inputs` and establishes the keys for the property `table` within its `truth_table`, where each key corresponds to a `boolean_constant_expression`. Note that the parameter `expression` of each `boolean_constant_expression` is formed by replacing the variables of the `truth_table`'s `expression`, in a alphabitical order, with it's corresponding key. To learn about what characters are considerd variables? or to learn about how a `truth_table`'s `expression` get replaced by its `inputs` [click here](#questions).
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

* `truth_table.has_header`: is a `bool` that is used to determine wether the header of a `valid` `truth_table` will be printed when `truth_table` gets printed.
  * By default it is set to `True` meaning that a `valid` `truth_table` would print like this:
    ```
     in  | B * !(A + C) + A | out
    -----|------------------|-----
     011 | 1 * !(0 + 1) + 0 |  0
     000 | 0 * !(0 + 0) + 0 |  0
     100 | 0 * !(1 + 0) + 1 |  1
     100 | 0 * !(1 + 0) + 1 |  1
    ```
  * When `has_header` is is false, a `truth_table` would be printed like this:
    ```
    011 | 1 * !(0 + 1) + 0 | 0
    000 | 0 * !(0 + 0) + 0 | 0
    100 | 0 * !(1 + 0) + 1 | 1
    100 | 0 * !(1 + 0) + 1 | 1
    ```
  * Note that when the `truth_table` is not `valid` the `truth_table` will print without header even if `has_header` has been set to `True`.
    * For example:
      ```
      from Truth_Table import truth_table
      from Boolean_Constant_Expresssion import boolean_constant_expresssion
            
      expression = "a * !b"
      
      table = truth_table(expression)
      
      print("valid: ", table.valid)
      print("has_header: ", table.has_header)
      print(table)
      
      print()
      
      table.table["01"] = boolean_constant_expresssion("1 + !1")
      print("valid: ", table.valid)
      print("has_header: ", table.has_header)
      print(table)
      ```
      ```
      valid:  True
      has_header:  True
       in | a * !b | out
      ----|--------|-----
       00 | 0 * !0 |  0
       01 | 0 * !1 |  0
       10 | 1 * !0 |  1
       11 | 1 * !1 |  0
      
      valid:  False
      has_header:  True
      00 | 0 * !0 | 0
      01 | 1 + !1 | 1
      10 | 1 * !0 | 1
      11 | 1 * !1 | 0
      ```
    
* `truth_table.output_format`: holds the output format that will be used when the `truth_table` gets printed.
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
    * the `dict` will hold `boolean_constant_expression`s, where the `expression` of each `boolean_constant_expression` will be the `truth_table`'s `expression` but with it's variables being replaced by the `boolean_constant_expression` `truth_table.table`'s key in a alphbetical order. To learn about what characters are considerd variables? or to learn about how a `truth_table`'s `expression` get replaced by its `inputs` [click here](#questions).
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
    * if `inputs` gets changed or set to a non-empty `list`, the `truth_table` will be regenerated with the new or updated `inputs`. To learn about what characters are considerd variables? or to learn about how a `truth_table`'s `expression` get replaced by its `inputs` [click here](#questions).
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

* `truth_table.valid`: is of type `bool`. It is used to determine whether `truth_table.table` has been edited manually.
  * When `truth_table.valid` is set to `True`: the `truth_table` gets recreated with the current `inputs`
    * Example:
      ```
      from Truth_Table import truth_table
      from Boolean_Constant_Expresssion import boolean_constant_expresssion
      
      expression = "A * B"
      
      tests = ["01", "11"]
      
      table = truth_table(expression, inputs = tests)
      
      print("Valid: ", table.valid)
      print(table)
      
      print()
      
      table.table["10"] = boolean_constant_expresssion("1 + 1")
      print("Valid: ", table.valid)
      print(table)
      
      print()
      
      table.valid = True
      print("Valid: ", table.valid)
      print(table)
      ```
      ```
       in | A * B | out
      ----|-------|-----
       01 | 0 * 1 |  0
       11 | 1 * 1 |  1
      
      Valid:  False
      01 | 0 * 1 | 0
      11 | 1 * 1 | 1
      10 | 1 + 1 | 1
      
      Valid:  True
       in | A * B | out
      ----|-------|-----
       01 | 0 * 1 |  0
       11 | 1 * 1 |  1
       10 | 1 * 0 |  0
      ```
### Questions

#### What characters are considered variables in a `expression`?

The variables in `expression` are any character in the `expression` that have an ASCII value that is in between 65-122 (A-Z or a-z).

#### How do the variables in a `expression` get replaced by its `inputs` in a `truth_table`?

The charcters for each `input` in `inputs` replaces the variables in `expression` depending on the alphetical order of the variables in `expression`. Meaing that in `expression` "B + A", the `input` "01", would replace the variable 'A' with 0 and the variable 'B' by 1 which would be be "1 + 0". 
