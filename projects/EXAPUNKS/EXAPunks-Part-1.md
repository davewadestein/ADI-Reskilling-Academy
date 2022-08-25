## EXAPUNKS Part 1: Basic operations

### Instructions

For the first part of the problem, we will be focusing on the very basic
features and instructions of the language.

(When you see __R/N__ below, it means that you can put a _register_ or a _number_ there.)

* __`COPY R/N R`__
<br>Copy the value of the first operand into the second operand.
* __`ADDI R/N R/N R`__ 
<br>Add the value of the first operand to the value of the second operand and store the result in the third operand.
* __`SUBI R/N R/N R`__
<br>Same as `ADDI`, for substraction.
* __`MULI R/N R/N R`__  
Same as `ADDI`, for multiplication.
* __`DIVI R/N R/N R`__  
Same as `ADDI`, for integral division.
* __`MODI R/N R/N R`__  
Same as `ADDI`, for modulo.
  
As you can see, all of the above operations put their result into a _register_, but the
operands can be either registers or numbers.

Here are a few parsing constraints:
* Any unknown instruction, register or invalid number should result in a crash
* Leading spaces (at the start of a line of code) should be safely ignored
* Empty lines should be ignored

Write a program that can understand a piece of code with any of the above
instructions and run it.

### Guidelines

1. It is generally a good idea to start by identifying the inputs and outputs
   of the program. Here, the input is the code for the EXA, which will be just
   plain text. No need to worry about outputs for now; printing the register
   values after each step should be enough. Don't hesitate to add more `print`
   lines as needed.

2. The first piece of code you'll need is one that can read a line of EXA code
   and make sense of it. For example, `"ADDI 30 X T"` could be converted into
   `("ADDI", [30, "X", "T"])` or any other structure of your choice. This will
   make it much easier to write the actual running logic. It is at this step
   that you could check if instructions and their operands are valid.

3. Before implementing the instructions, think about how you want to handle
   the registers. Here are some suggestions:
   * Just use variables to represent the registers
   * Try a functional approach, where the current register values is passed to
     functions which represent the instructions; those functions then return the new
     values of the registers
   * Try an object-oriented approach–with this kind of solution, the registers
     `X` and `T` could be attributes of an EXA object

4. If you manage to design the code parsing and register handling carefully,
   actually implementing the instructions should be fairly easy! The only
   detail is that you will need to be careful about whether an argument is a
   number or a register name when both are allowed, and choose the correct
   behavior.
   
5. While it's fine to have global variables, for example, for the registers, I
recommend that you have functions that access those variables so that in other 
modules (files) you can call those functions to set the registers and get their
values.

6. I would recommend breaking this up into multiple files (modules).

### Example

Here is an example:

    COPY 70 X
    ADDI X 1 X
    COPY 3 T
    MULI T X T
    SUBI T 1 T

Decomposed, this program will:

1. Set `X` to 70
2. Add 1 to the value of `X` and store that value back in `X`
3. Set `T` to 3
4. Multiply `X` by `T` and store that value in `T`
5. Substract 1 from `T` and store the result in `T`

At the end, `X` should hold 71 and `T` should hold 212.

### Challenge

Here is another example for you to try your code on:

    COPY 647 X
    MODI X 7 T
    DIVI X T X
    MULI T T T
    MULI X T X
    MULI T T T
    ADDI X T X
    DIVI T 9 T
    ADDI X 3 X
    ADDI T X T
    ADDI T X X
    SUBI X T T
    SUBI X T X
    SUBI X T X

What are the values of the registers at the end? As a bonus, can you identify
what operation the last five instructions are effectively doing?

[Part 2](https://github.com/davewadestein/ADI-Learn-to-Code/blob/main/projects/EXAPUNKS/EXAPunks-Part-2.md)

## Thoughts on algorithm
* read the file a line at a time
* skip if empty line
* validate the instruction (first word on the line...COPY, ADDI, etc.)
  * if word is not in my list of valid instructions then bail out
  * import sys ... sys.exit(1) # terminate the program
  * otherwise, it's valid and COPY is the odd one out (takes 2 arguments vs. 3 arguments)
  * count the number of arguments on the line and be sure it's 3 or 4 as needed
    * if not correct, then bail out

```
  valid_commands = 'COPY ADDI ...'.split() # this could be a tuple or some other container

  def COPY(arguments): # words[1:], i.e., the slice of the original line which excludes the instruction

  def validate_args(num_args, ... ) #: pass in "blueprint" for these arguments
      # this function's job might be to validate number of args
      # and "type" of arguments (i.e., they are numbers when they should be and
      # registers when they should be)
      if len(arguments) != num_args: # not valid for COPY
          CRASH!
      # COPY R/N R
      # How do I know that argument[1] is a Register?
      # COPY(['X', 'FOO'])
      
      # classify each argument as register or number

      if we expect a register only and arg not in valid_registers: # [ 'X', 'T' ]
          CRASH!

      # if we can accept a number here, how do we know it's a number?
      try:
          arg = int(arg) # attempt to int-ify the argument
          # we found a number!
      except ValueError:
          # this is not a number, so CRASH!

      # suppose the command was COPY T X and T has 25 in it right now
      return tuple of the validated args converted to operands... (25, 'X')
```
