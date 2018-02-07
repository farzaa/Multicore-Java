import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;

public class Stack {

    AtomicInteger numOps = new AtomicInteger(0);
    AtomicReference<Node> head = new AtomicReference<Node>();

    class Node {
        Integer val;
        Node next;

        Node(Integer _val) {
            val = _val;
        }
    }

    public Stack() {
        head.set(null);
    }

    public Boolean push(Integer x) {
        Node localHead = head.get();

        // We want a new node ot push.
        Node brandNewNode = new Node(x);
        brandNewNode.next = localHead;

        // create a local copy to make sure we are looking at the right head.
        while(true) {
            if (head.compareAndSet(localHead, brandNewNode)) {
                numOps.getAndIncrement();
                break;
            }
        }
        return null;
    }

    public Integer pop() {
        // Check if head is null.
        // Get head, pop, -- num ops.
        if (head.get() == null) {
            return null;
        }
        // TODO: Can't head change here?
        head.set(head.get().next);

        numOps.getAndIncrement();
        return 0;
    }

    public int getNumOps() {
        return numOps.get();
    }


    public static void main(String args[]) {
        Stack s = new Stack();
        s.pop();
        s.push(1);
        s.push(2);
        s.push(3);
        s.push(1);
        s.push(2);
        s.push(3);
        s.pop();

        Node headOfStack = s.head.get();
        while(headOfStack != null) {
            System.out.println(headOfStack.val);
            headOfStack = headOfStack.next;
        }

        System.out.printf("NumOps... %d\n", s.numOps.get());
    }

}
