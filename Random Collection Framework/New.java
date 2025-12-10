import java.util.ArrayList;
import java.util.*;

public class New {
    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>();
        values.add(0);
        values.add(1);
        values.add(2);
        values.add(3);
        values.add(4);

        System.out.println("Print values using Iterator");
        Iterator<Integer> iteratorvalues = values.iterator();
        while(iteratorvalues.hasNext()){
            int val = iteratorvalues.next();
            System.out.println(val);
            if(val==3){
                iteratorvalues.remove();
            }
        }

        System.out.println("Print values using For each Loop");
        for (int val : values) {
            System.out.println(val);
        }
        
    }
}
