public class fan {
    int price;
    String color;
    String Brand;
    int no_of_wing;

    void startin(){
        System.out.println("brand name");

    }
    void roatating(){
        System.out.println("its roatating");

    }
    void blowing(){
        System.out.println("its blowinf");

    }
    void stoping(){
        System.out.println("its stoping");

    }
    public static void main (String[]args){
        fan f1 = new fan();
        fan f2 = new fan();
        f1.startin();
        f1.blowing();
        f2.roatating();
        
    }
}

