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


}

public class Main {
    public static void main(String args[]) {
        System.out.println("Starting app");
        
	Adder adder = new Adder(10, 20);
	System.out.println("The result... "+adder.add()
			)
        System.out.println("App finished.");
    }
}
