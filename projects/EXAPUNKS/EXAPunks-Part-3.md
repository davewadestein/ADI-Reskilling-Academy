## EXAPUNKS Part 3: Labels and Jumps

### Instructions

So far our program pointer only moves through the program from top to bottom,
and doen't have much in the way of actual logic. Time to introduce some useful
flow control instrustions:

* `MARK L`  
  Mark this line with the specified label. `MARK` is a pseudo-instruction and
  is not executed. If this label already exists, then this is an invalid instruction.
* `JUMP L`  
  Jump to the specified label.
* `TJMP L`  
  Jump to the specified label if the `T` register equals 1 (or any value other
  than 0). This corresponds to a `TEST` result that was true.
* `FJMP L`  
  Jump to the specified label if the `T` register equals 0. This corresponds
  to a `TEST` result that was false.

If the same label is marked multiple times, the program is entirely invalid
and should fail to parse or compile.

*Note:* Be careful to not write any infinite loops!

### Example

Let me walk you through a simple example:

    COPY 1 X
    COPY 7 T
    MARK LOOP
    MULI T X X
    SUBI T 1 T
    TJMP LOOP

1. Set `X` to 1
2. Set `T` to 7.
3. Line 4 gets marked as `LOOP`.
4. Multiply `X` by `T` and store that in `X`.
5. Decrease `T` by 1.
6. If the value of `T` is not 0, jump back to `LOOP` (step 4.).

This effectively calculates 7! ([factorial] of 7), which should be 5040.

[factorial]: https://en.wikipedia.org/wiki/Factorial

### Challenge

Can you implement an EXA program that tests the [Collatz conjecture] for a number
of your choice? It doesn't need to output the number of steps or anything, for
now try to implement a program that goes through the sequence until it ends.

[Collatz conjecture]: https://en.wikipedia.org/wiki/Collatz_conjecture

[Part 4](https://github.com/davewadestein/ADI-Learn-to-Code/blob/main/projects/EXAPUNKS/EXAPunks-Part-4.md)
