# Solution

The intentional solution is writing a symbolic execution engine for Whitespace language. However, it is also possible to decompile Whitespace to C and compile the C code with compiler optimizations to get a clearer native file which can be attacked via angr.

I have written my symbolic execution engine called [whitesymex](//github.com/umutoztunc/whitesymex). The flag can be obtained via whitesymex:

```sh
$ whitesymex --find 'crewmember' --avoid 'Imposter!' spaceship.ws
# xctf{Wh1t3sym3x!?}
```

It takes around 3-5 minutes. However, it is possible to get a solution which takes approximately 10 seconds using whitesymex python API. You need to find the text message that will be printed for the correct input which can be found with some static analysis. You also need to find the flag length which can be found using both static and dynamic analysis. The code for this solution is [here](solve.py).
