To run these files, its the same process as problem_1

Simply have Python 3.6 and run:

python problem_2_v1.py

For all four versions of the program.

Version 1:
This one dead locks! This occurs when each philosophers each picks up their left fork and end up never getting the right
fork! If you run the program the print statements will show this.

Version 2:
This one doesn't deadlock, but COULD cause big time starvation depending on the scheduler! My solution was to allow the philosopher acquire the
left stick, then if they can acquire the right stick, they can eat. But if they can't get the right stick, then they release the left stick, don't eat,
and once again begin waiting to eat.

Version 3:
To get around the starvation issue, after a philosopher eats he sleeps for a random number of seconds between 5 and 10.
If a philosopher isn't able to eat he waits for a random number of seconds between 0 and 1. While this has its issues,
it ensure every philosopher can eat at one point. It also makes everything seem much more organized since the philosophers
threads aren't context switching as randomly due to the sleep. Note: you'll notice that the threads start in order, and then start getting
jumbled around later!

Version 4:
To run a command line argument to change the number of philosophers, simply give:
python problem_2_v4.py -num=10
