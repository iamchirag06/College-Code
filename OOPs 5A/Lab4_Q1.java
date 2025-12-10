public class Lab4_Q1 {
    public static void main(String[] args) {
        A obj = new A(2,4);
        obj.show();

    }
}
class A{
    int age;

    public A(){
        System.out.println("In Constructor");
    }

    public A(int n1,int n2){
        System.out.println("In Parametrzed Constructor");
    }

    public void show(){
        System.out.println("In Method...");
    }
}