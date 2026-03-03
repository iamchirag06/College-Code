import java.util.*;

public class QueueExample {
    public static void main(String[] args) {
        Queue<String> q = new LinkedList<>();

        q.offer("A");
        q.offer("B");
        q.offer("C");

        System.out.println(q);          // [A, B, C]
        System.out.println(q.peek());   // A (head element)
        System.out.println(q.poll());   // removes A
        System.out.println(q);          // [B, C]


       
}