
import java.util.Scanner;

public class Lab2_Q1 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter an Integer:");
            int input = sc.nextInt();
            
            IntegerChecker checker = new IntegerChecker(input);
            checker.displayResult();
        }
    }

    public static abstract class NumberChecker<T> {
        protected T number;

        public NumberChecker(T number) {
            this.number = number;
        }

        public abstract boolean isEven();

        public void displayResult() {
            System.out.println("Number entered: " + number);
            if (isEven()) {
                System.out.println(number + " is Even.");
            } else {
                System.out.println(number + " is Odd.");
            }
        }
    }

    public static class IntegerChecker extends NumberChecker<Integer> {
        public IntegerChecker(Integer number) {
            super(number);
        }

        @SuppressWarnings("override")
        public boolean isEven() {
            return number % 2 == 0;
        }
    }
}