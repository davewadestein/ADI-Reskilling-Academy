
# EXAPUNKS Emulator (Adapted for ADI Learn to Code project)

## Introduction

[EXAPUNKS] is a 2018 video game by Zachtronics. It is set in a cyberpunk past
where all technology works using swarms of small programs, known as EXAs
(EXecution Agents). The principle of the game is to program your EXAs using an
assembly-like language, and accomplish various (illicit) jobs. 

For today's coding challenge, we will be building a simulator that can read and
execute a program written in the EXA language.

[EXAPUNKS]: http://www.zachtronics.com/exapunks/

_Disclaimer: EXAPUNKS and its contents, including the EXA language and the
excerpts from the TRASH WORLD NEWS manual used in this document, are a
property of Zachtronics LLC._

## EXA fundamentals

> Every EXA contains **code** and **registers**.  
> **CODE:** This is a list of instructions that tell an EXA what to do. It's
> written in a special computer language specifically designed for them. We'll
> dig into the language in the following sections.   
> **REGISTERS:** Think of these are slots that can store numbers. Registers
> can be read and written to by instructions in your code. 

An EXA has three registers:

* The `X` register is a general-purpose storage register. It can store a
  number and initially contains 0.
* The `T` register is a general-purpose storage register like `X`. It is also
  the destination for `TEST` instructions ([Part 2]), and is the
  criterion for conditional jumps ([Part 3]).
* A file handling register named `F`. Its operation will be detailed in
  [Part 4].

Through every instruction description in this challenge, the following
abbreviations will be used to represent required operands:

* `R`: A register
* `R/N`: A register, or a number between -9999 and 9999
* `L`: A label defined by a `MARK` pseudo-instruction (see [Part 3])

### You will be coding this along with a partner, one part at a time.
### DO NOT ATTEMPT A PART UNTIL YOU'VE COMPLETED THE PREVIOUS PART!

[Part 1](https://github.com/davewadestein/ADI-Learn-to-Code/blob/main/projects/EXAPUNKS/EXAPunks-Part-1.md)

[Part 2](https://github.com/davewadestein/ADI-Learn-to-Code/blob/main/projects/EXAPUNKS/EXAPunks-Part-2.md)

[Part 3](https://github.com/davewadestein/ADI-Learn-to-Code/blob/main/projects/EXAPUNKS/EXAPunks-Part-3.md)

[Part 4](https://github.com/davewadestein/ADI-Learn-to-Code/blob/main/projects/EXAPUNKS/EXAPunks-Part-4.md)

# Our process should be as follows:
0. the entire process should be infused with the idea that we are working together
1. understand the problem
2. identify major components (modules) / pseudocode to explain how they communicate 
3. identify functions (and how they will work) to perform the tasks noted in step 2 (possibly stub them out)
4. do TDD per module, group like functions in TDD together (generate test_*.py files)
5. make tests pass, you can decide who does what
6. put it all together and run the tests here
