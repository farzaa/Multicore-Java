import java.util.concurrent.atomic.AtomicInteger;

public class StackMain<T> extends Thread {
    static Stack stack = new Stack();
    static AtomicInteger numDone = new AtomicInteger(0);
    static AtomicInteger operations = new AtomicInteger(0);

    static int THREAD_COUNT = 10;


    public static void main(String args[]){

        for (int i = 0; i < THREAD_COUNT; i++) {
            Thread thread = new StackMain();
            int id = (int) thread.getId();
            // the easiest thing to do is refer to our thread by its system ID.
            System.out.println("Starting thread with id... " + id);
            thread.start();
        }

        // wait until our threads are done.
        while (numDone.get() != THREAD_COUNT);

        // at this point all threads have returned.
        // operations is the count of the number of operations we passed to the stack.
        // numOps is the number of operations the stack itself counted.
        // if these are equal, life is good and the program did its job in a lockless manner.
        if (stack.numOps.get() == operations.get()) {
            System.out.println("Success!");
        }
    }

    @Override
    public void run() {
        int id = (int) Thread.currentThread().getId();
        // for every thread, spawn some pop and push operations.
        for(int i = 0; i < 1000; i++) {
            if (i % 3 == 0) {
                // only increment the counter if we didn't get back null!
                if (stack.pop() != null) {
                    operations.getAndIncrement();
                }
            } else {
                stack.push(i);
                operations.getAndIncrement();
            }
        }

        numDone.incrementAndGet();
    }
}
