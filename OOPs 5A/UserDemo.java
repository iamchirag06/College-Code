class User {
    private String name;
    private int age;
    private boolean isActive;

    // Constructor with default values
    public User() {
        this.name = "Guest";
        this.age = 18;
        this.isActive = true;
    }

    // Constructor with custom values
    public User(String name, int age, boolean isActive) {
        this.name = name;
        this.age = age;
        this.isActive = isActive;
    }

    public String greet() {
        return "Hello, " + name + "!";
    }

    // Getters
    public String getName() { return name; }
    public int getAge() { return age; }
    public boolean isActive() { return isActive; }
}

public class UserDemo {
    public static void main(String[] args) {
        
        User defaultUser = new User(); // Uses default values
        System.out.println(defaultUser.greet()); // Hello, Guest!
        System.out.println("Name: " + defaultUser.getName());
        System.out.println("Age: " + defaultUser.getAge());
        System.out.println("Active: " + defaultUser.isActive());

        System.out.println();

        User customUser = new User("Alice", 25, false); // Uses provided values
        System.out.println(customUser.greet()); // Hello, Alice!
        System.out.println("Name: " + customUser.getName());
        System.out.println("Age: " + customUser.getAge());
        System.out.println("Active: " + customUser.isActive());
    }
} 