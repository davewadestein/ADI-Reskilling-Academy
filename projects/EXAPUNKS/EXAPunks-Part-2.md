## EXAPUNKS Part 2: Tests

We mentioned earlier that the `T` register was used for tests. This part of
the challenge will be to program the `TEST` instruction:

* `TEST R/N = R/N`  
  Compare the value of the first operand to the value of the second operand.
  If they are equal, set the `T` register to 1, otherwise set the `T` register
  to 0. The same syntax is used for the `<` (less than) and `>` (greater than)
  tests. 

Here is an example of `TEST`:

    COPY 10 X
    COPY X T
    TEST X = T
    SUBI X T T
    TEST X > T
    TEST T < 1

This will:

1. Set `X` to 10
2. Set `T` to the value of `X`
3. Test if `X` and `T` are equal. This is true, so `T` is set to 1.
4. Substract `T` from `X`, store it in `T` (now 9).
5. Test if `X` is greater than `T`. This is true again, `T` is set to 1.
6. Finally, test if `T` is smaller than 1. This is false, so `T` is set to 0.

So far it might not look very useful, but the next part will fix that.

[Part 3](https://github.com/davewadestein/ADI-Learn-to-Code/blob/main/projects/EXAPUNKS/EXAPunks-Part-3.md)
