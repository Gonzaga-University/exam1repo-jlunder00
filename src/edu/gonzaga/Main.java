package edu.gonzaga;

class Adder<T extends Number> {
    T val1;
    T val2;

    public Adder(T new_val1, T new_val2) {
        val1 = new_val1;
        val2 = new_val2;
    }


}

public class Main {
    public static void main(String args[]) {
        System.out.println("Starting app");
        Adder adder = new Adder(10, 20);

        System.out.println("App finished.");
    }
}
