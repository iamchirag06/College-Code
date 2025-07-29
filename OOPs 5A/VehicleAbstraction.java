
// Example 1: Vehicle Abstraction
public class VehicleAbstraction {
    public static void main(String[] args) {
        Vehicle car = new Car();
        Vehicle bike = new Bike();

        car.start();
        car.fuelType();
        car.stop();

        bike.start();
        bike.fuelType();
        bike.stop();
    }
}
abstract class Vehicle {
    abstract void start();
    abstract void stop();

    void fuelType() {
        System.out.println("All vehicles need fuel.");
    }
}

class Car extends Vehicle {
    void start() {
        System.out.println("Car starts with a key.");
    }
    void stop() {
        System.out.println("Car stops with brakes.");
    }
}

class Bike extends Vehicle {
    void start() {
        System.out.println("Bike starts with a kick or button.");
    }
    void stop() {
        System.out.println("Bike stops with hand brakes.");
    }
}

