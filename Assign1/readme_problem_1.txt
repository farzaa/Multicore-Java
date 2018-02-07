Hello.

This is a simple Python 3.6 program. To run, make sure you have v 3.6 and simply run it by doing:
python problem_1.py

After that, it will output a prime.txt file within the directory it was run.

Note #1  - WHY IS IT SO SLOW?
The runtime, because it being Python, is MUCH higher than if the program was written in other languages like Java. This is all because Python is a much higher level language
It is a well known fact that equivalent C code will run up to 10 - 100 times faster. Also, Python interprets the code at runtime vs something like Java where the JIT compiler
will compile things for you into native byte code. TLDR: Python has to go through many more layers of abstraction.


I start the timer after the massive Sieve array is allocated. I stop the timer after the main thread stops. The program itself runs in about 40 seconds total on my old i5
2012 MacBook. Around 12 seconds to allocate the sieve, 13 seconds to run the Sieve, and 15 seconds to actually do things like count the primes and sum them.

Note #2
Runtime with 1 thread - 28357.98
Runtime with 8 threads - 27177.0

The speedup was minimal despite spreading out the work equally.

Proof:
The professor asked for some proof for why I think my program is right. Well, I'm using a basic sieve of eratosthenes
which is a well known algorithm. Implementing this in Python is trivial, I ran my program with the simple sieve and got
an answer and saved it. I also used a Python sieve implementation I found online to compare my answer, and got the same one.
I then used multiple threads and use some simple math tricks to cut down on the amount of computation and still arrived
at the right answer. After doing this, I still arrive at the right answer.
