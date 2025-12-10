import java.util.*;

public class DequqeInterface {
    public static void main(String[] args) {

        Deque<String> deq = new LinkedList<>();

        // add / addFirst / push
        deq.add("Ele 1");            // add at last
        deq.addFirst("Ele 2");       // add at first
        deq.addLast("Ele 3");        // add at last
        deq.push("Ele 4");           // add at first (stack style)

        // add last
        // deq.addLast("Ele 5");
        
        // add first safely
        deq.offerFirst("Ele 6");

        System.out.println("Deque is: " + deq);

        // removing elements
        deq.removeFirst();
        deq.removeLast();

        System.out.println("After removing first & last: " + deq);
    }
}
