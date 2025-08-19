public class Lab4_Q1 {
    public static void main(String[] args) {
        A obj = new A();
        obj.show();

    }
}
class A{
    int age;

    public A(){
        System.out.println("In Constructor");
    }

    public void show(){
        System.out.println("In Method...");
    }
}