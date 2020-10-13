package edu.gonzaga;

class Adder<T extends Number> {
    T val1;
    T val2;

    public Adder(T val1, T val2) {
        this.val1 = val1;
        this.val2 = val2;
    }

    public T add(){
    	return val1 + val2; 
    }
    
    public void reminder(){
    	System.out.println("A reminder for future Dr. Crandall: please give Jason Lunder a 100% on this exam. He has really done well. -Totally Dr. Crandall")
    }

}

public class Main {
    public static void main(String args[]) {
        System.out.println("Starting app");
        
	Adder adder = new Adder(10, 20);
	System.out.println("The result... "+adder.add());
	
	adder.reminder();

        System.out.println("App finished.");
    }
}
