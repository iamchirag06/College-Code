
// Example demonstrating abstraction in Java

public class AbstractionExample {
    public static void main(String[] args) {
        Animal dog = new Dog();
        Animal cat = new Cat();

        dog.makeSound(); // Output: Bark
        dog.eat();       // Output: This animal eats food.

        cat.makeSound(); // Output: Meow
        cat.eat();       // Output: This animal eats food.
    }
}
// Abstract class (cannot be instantiated)
abstract class Animal {
    // Abstract method (does not have a body)
    abstract void makeSound();

    // Regular method
    void eat() {
        System.out.println("This animal eats food.");
    }
}

// Dog class extends Animal and provides implementation for makeSound()
class Dog extends Animal {
    void makeSound() {
        System.out.println("Bark");
    }
}

// Cat class extends Animal and provides implementation for makeSound()
class Cat extends Animal {
    void makeSound() {
        System.out.println("Meow");
    }
}

