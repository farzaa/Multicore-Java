import time
import queue as queue
from threading import Thread
import threading
import logging
import math

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

LIMIT = 10**8
s = time.time()

logging.debug("Intializing sieve array...")
# First lets initialize the entire array to True.
# I create the array and ignore the evens right off the bat.
# Thus, halving the size.
# I also use a bytearray so the memory footprint is lower.
# sieve = bytearray([True]) * (n//2)
sieve = [True] * LIMIT
sieve[0] = sieve[1] = False
for i in range(4, len(sieve), 2):
    sieve[i] = False


logging.debug('Time to intialize Sieve array in seconds: ' + str(time.time() - s))

len_sieve = len(sieve)

# Lists are thread safe in python, SORT OF.
# The data is not 100% safe. So, we can access the data from different threads.
# But setting the data is not! Though in my case, I use a queue to fix this.
job_queue = queue.Queue()

def do_sieve(job_queue):
    while True:
        num_to_proccess = job_queue.get()
        # print(sieve)
        print(num_to_proccess)
        n = num_to_proccess
        # This //2 is to adjust for the fact that our array is HALF the size.
        if sieve[num_to_proccess]:
            # This is where the magic happens!

            # Just for reference, I found a solution on StackOverflow that brings the runtime
            # Of this code down to 0.5 seconds with some very clever math tricks.
            # I didn't use it because I didn't quite understand most of them.
            # https://stackoverflow.com/a/46635266/7175326

            # n*n is a clever math trick to help us start looking for primes at the right spot.
            for j in range(n*n, len_sieve, 2*n):
                sieve[j] = False
        job_queue.task_done()


# Declare all threads once up here! I don't constantly create/destroy arrays.
for i in range(1):
    worker = Thread(target=do_sieve, args=(job_queue,))
    worker.setDaemon(True)
    worker.start()

s = time.time()
# This actually creates the jobs! I found the LIMIT**0.5 online.
# It's a well known math trick and massively speeds this up because
# We don't need to look through all 10**8 nums.
for num_to_proccess in range(3, int(LIMIT**0.5), 2):
    job_queue.put(num_to_proccess)

# This waits on the job_queue to empty!
job_queue.join()

logging.debug('Done with Sieve' + str(time.time() - s))
print("Counting and doing post Sieve work...")
counter = 0
prime_sum = 0
for i in range(len_sieve):
    if sieve[i]:
        counter += 1
        prime_sum += i

# Grab last 10 primes.
last = []
for i in range(len_sieve - 1, -1, -1):
    if sieve[i]:
        last.append(i)
    if len(last) == 10:
        break

print(last)
last.reverse()

total_exec_time = round((time.time() - s) * 1000, 0)
f = open('primes.txt', 'w')
f.write(str(total_exec_time))
f.write(' ')
f.write(str(counter))
print(counter)
f.write(' ')
f.write(str(prime_sum))
f.write(' ')
for num in last:
    f.write(str(num))
    f.write(' ')
f.close()
