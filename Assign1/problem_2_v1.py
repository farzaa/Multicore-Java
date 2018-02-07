import threading



# In order to organzize all this data related to a philosopher
# I simply create an object.

class PhilThread(threading.Thread):
    def __init__(self, phil_id, left_stick, right_stick):
        threading.Thread.__init__(self)
        self.phil_id = phil_id
        self.left_stick = left_stick
        self.right_stick = right_stick
        # Start thread running by default!
        self.running = True

    def run(self):
        # this infinitely runs until the actual thread stops.
        while(self.running):
            print("%d is now thinking" % self.phil_id)
            # go and try to eat!
            self.eat()

    def eat(self):
        print("%d is now hungry" % self.phil_id)
        # First get lock object references!
        left = self.left_stick
        right = self.right_stick

        # Now actually get the locks. This can cause a deadlock!
        left.acquire()
        right.acquire()
        print("%d is now eating" % self.phil_id)
        left.release()
        right.release()


def main():
    # First lets create the forks, which are really just going to be resources with locks.
    # Version of this program demands that no two philosophers hold the same chopstick at the same time.
    # This is easy with locks :)!

    # First make the locks.
    shared_objects = []
    for i in range(5):
        shared_objects.append(threading.Lock())

    phils = []
    # Then, assign them to PhilThread's we create.
    for i in range(5):
        # its a circular table, so theres a special case there so the array of locks wrap!
        if i == 4:
            phils.append(PhilThread(i, shared_objects[i], shared_objects[0]))
            break
        phils.append(PhilThread(i, shared_objects[i], shared_objects[i+1]))

    for phil in phils:
        phil.start()

main()
