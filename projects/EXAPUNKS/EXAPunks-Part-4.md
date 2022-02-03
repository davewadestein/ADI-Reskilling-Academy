## EXAPUNKS Part 4: File handling

### Instructions

All that programming is no good if it cannot input and output. Thankfully, EXAs
can manipulate files and leave traces.

In our simplified emulator, a file is simply a list of numbers with a name.
To use a file, an EXA must first grab that file by its name. Once done, it has
to drop it before using a different file.

Here is also where the `F` register comes in play. The reference guide reads:

> The `F` register allows an EXA to read and write the contents of a held file.
> When an EXA grabs a file, its "file cursor" will be set to the first value in
> the file. Reading from the `F` register will read this value; writing to the
> `F` register will overwrite this value. After reading or writing the `F`
> register, the file cursor will automatically advance. Writing to the end of
> the file will append a new value instead of overwriting.

*Note:* This is **not** the same file handling as the one you'd do with `open`
in Python. These files are virtual; lists which exist only in the emulator.
You will need to add them to your simulation.

The file manipulation instructions to implement are:

* `GRAB R/N`  
  Grab a file with the specified ID.
* `FILE R`  
  Copy the ID of the file into the specified register.
* `SEEK R/N`  
  Move the file cursor forward (positive) or backwards (negative) by the
  specified number of values. If `SEEK` would move the file cursor past the beginning or end of the file
  it will instead be clamped. Thus, you can use values of -9999 or 9999 to
  reliably move to the beginning or end of a file.
* `VOID F`  
  Remove the value highlighted by the file cursor from the currently held file.
* `DROP`  
  Drop the currently held file.
* `TEST EOF`  
  If the file pointer is currently at the end of the held file, set the `T`
  register to 1, otherwise set the `T` register to 0. 

Note that trying to access this register when the EXA isn't holding a file will
result in an "Invalid `F` register access" error, causing the EXA to crash and
terminate. If an EXA tries to open a file that does not exist (or is otherwise
not available), it also crashes.

Modify your emulator to support file handling. On top of the code to run, it
will need to be initialized with files (and their contents). It will need to
return the file contents at the end of execution.

### Example

Let's look at a simple file handling program. In this scenario, the environment
starts with two existing files: one called 100 with a list of numbers, and a
second one called 200 that's empty.

    GRAB 100
    MARK FILE_READ
    ADDI F X X
    TEST EOF
    FJMP FILE_READ
    DROP
    GRAB 200
    COPY X F
    DROP

This time, try to walk through the instructions yourself. This script reads the
numbers in 100, sums them, and writes the sum to 200.

### Final Challenge

Here's the final code to test your emulator against. The virtual
world is expected to contain a file with the ID 400 that is initially empty.

    GRAB 400
    COPY 1 X
    MARK A
    SEEK -9999
    ADDI X 1 X
    TEST X < 50
    FJMP D
    MARK B
    TEST EOF
    TJMP C
    MODI X F T
    FJMP A
    JUMP B
    MARK C
    COPY X F
    JUMP A
    MARK D
    DROP

What are the contents of the file 400 at the end of the program? Can you
identify what calculation this program is doing?
