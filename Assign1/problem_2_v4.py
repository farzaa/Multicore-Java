import threading
import time
from random import *
import os
import argparse
import sys
from threading import Thread

parser = argparse.ArgumentParser()
parser.add_argument(
    '-num',
    type=int)

# In order to organzize all this data related to a philosopher
# I simply create an object.

class PhilThread(threading.Thread):
    running = True
    def __init__(self, phil_id, left_stick, right_stick):
        threading.Thread.__init__(self)
        self.phil_id = phil_id
        self.left_stick = left_stick
        self.right_stick = right_stick
        # Start thread running by default!

    def run(self):
        # this infinitely runs until the actual thread stops.
        while(self.running):
            print("%d is now thinking" % self.phil_id)
            # go and try to eat!
            self.eat()

    def eat(self):
        print("%d is now hungry" % self.phil_id)
        # This is inly here
        # First get lock object references!
        left = self.left_stick
        right = self.right_stick

        left.acquire(True)
        # To get around the problem of deadlock, pick up both forks only if we can
        # pick up the left fork and then the right fork.
        # if we can't pick up the right, drop it.

        if right.acquire(False) is False:
            left.release()
            time.sleep(random.uniform(0, 1))
            return

        print("%d is now eating" % self.phil_id)

        left.release()
        right.release()

        time.sleep(randint(5,10))


def get_out():
    run = True
    while(run):
        n = input()
        if n == "n":
            print("You typed n!")
            run = False
    os._exit(1)
def main():

    args = parser.parse_args()
    NUM_PHILOSOPHERS = args.num

    # First lets create the forks, which are really just going to be resources with locks.
    # Version of this program demands that no two philosophers hold the same chopstick at the same time.
    # This is easy with locks :)!
    time.sleep(1.0)
    # First make the locks.
    shared_objects = []
    for i in range(NUM_PHILOSOPHERS):
        shared_objects.append(threading.Lock())

    phils = []
    # Then, assign them to PhilThread's we create.
    for i in range(NUM_PHILOSOPHERS):
        # its a circular table, so theres a special case there so the array of locks wrap!
        if i == NUM_PHILOSOPHERS - 1:
            phils.append(PhilThread(i, shared_objects[i], shared_objects[0]))
            break
        phils.append(PhilThread(i, shared_objects[i], shared_objects[i+1]))

    t = Thread(target=get_out)
    t.setDaemon = True
    t.start()

    for phil in phils:
        time.sleep(0.5)
        phil.start()




main()
