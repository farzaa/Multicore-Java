import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;

public class Stack<T> extends Thread{

    AtomicInteger numOps = new AtomicInteger(0);
    AtomicInteger popCounter = new AtomicInteger(0);

    // keep just one reference to the head!
    AtomicReference<Node> head = new AtomicReference<Node>();

    int id = (int) Thread.currentThread().getId();

    class Node {
        T val;
        Node next;

        Node(T _val) {
            val = _val;
        }
    }

    public Stack() {
        head.set(null);
    }

    public Boolean push(T x) {
        Node brandNewNode = new Node(x);
        while(true) {
            // create a local copy of head.
            // i do this to make sure the value of localHead does not change
            // within the scope of the function even if the actual head changes.
            // also, move the next pointer of our new node to localHead.
            Node localHead = head.get();
            brandNewNode.next = localHead;

            // we ONLY want to swap heads if the head is == to our localHead we created.
            // if its not, we know that some other thread interrupted and changed our head.
            // in the case, this compareAndSet will FAIL.
            if (head.compareAndSet(localHead, brandNewNode)) {
                System.out.println("Pushed... " + brandNewNode.val);
                numOps.getAndIncrement();
                break;
            }
        }

        return true;
    }

    public T pop() {
        // this is where it gets tricky.
        // the pop function may get interrupted at any moment.
        while(true) {
            Node localHead = head.get();
            if (localHead == null) {
                return null;
            }

            // this is a strategy i found online
            // int localPopCount = popCounter.get();
            // where a pop counter is used to make sure we don't set the wrong head, but i actually don't see the point here.
            // we can easily do this by simply checking the memory address of head with that of localHead
            // if these don't match, then just try again later.
            if(head.compareAndSet(localHead, localHead.next)) {
                System.out.println("Popped... " + localHead.val);
                numOps.getAndIncrement();
                return localHead.val;
            }
        }
    }

    public Integer getNumOps() {
        return numOps.get();
    }

}
