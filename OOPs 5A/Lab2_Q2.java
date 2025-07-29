

abstract class StudentRecord {

    // Abstract method (no body) — specification abstraction
    public abstract void showFees();

    // Concrete method — implemented
    public void showInfo() {
        String name = "Raj";
        int rollNo = 12;
        System.out.println("Student Name: " + name);
        System.out.println("Roll Number: " + rollNo);
    }
}

// Subclass extends abstract class
class CollegeStudent extends StudentRecord {
    // Implementing abstract method
    public void showFees() {
        int fees = 50000;
        System.out.println("College Fees: Rs" + fees);
    }
}

// Main class
public class Lab2_Q2 {
    public static void main(String[] args) {
        // Creating object of subclass
        CollegeStudent student = new CollegeStudent();
        // Calling methods
        student.showInfo(); // from abstract class
        student.showFees(); // implemented in subclass
    }
}
