public class Lab_Q2 {
    public static void main(String[] args) {
        B obj = new B(10100,"Scorpio");
        obj.car();
    }
}
class B{

    private int price;
    private String brand;
    
   
    public B(int price, String brand) {
        this.price = price;
        this.brand = brand;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public void car(){
        System.out.println(brand);
        System.out.println(price);
    }
    
}