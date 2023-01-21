package Programmer.familiarityWithJava.homeWork1;

public class task3 {
    public static void main(String[] args) {
        boolean simple;
        System.out.print("Simple numbers from 2 to 100: ");
        for (int i = 2; i <= 100; i++){
            simple = true;
            for (int j = 2; j <= i/2; j++){
                if (i % j == 0) simple = false;
            }
            if (simple == true) System.out.print(Integer.toString(i) + " ");
        }
        System.out.println();
    }
}
