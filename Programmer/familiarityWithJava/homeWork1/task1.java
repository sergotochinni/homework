package Programmer.familiarityWithJava.homeWork1;

import java.util.Arrays;
import java.util.Scanner;

public class task1 {
    public static void main(String[] args) {
        // init the variable of class Scanner
        Scanner scn = new Scanner(System.in);
        // print hint
        System.out.print("Enter the length of array: ");
        // get value
        int ln = scn.nextInt();
        // close the object because it is no longer needed
        scn.close();
        // init array 
        double[] ar = new double[ln];
        // fill array with random values
        for (int i = 0; i < ln; i++){
            ar[i] = Math.random() * 300;
        }
        // init variables
        double max = ar[0];
        double min = ar[0];
        double avg = ar[0];
        // find min, max and summ of all elements
        for (int i = 1; i < ar.length; i++){
            avg = avg + ar[i];
            if (ar[i] > max) max = ar[i];
            if (ar[i] < min) min = ar[i];
        }
        // calculate the average
        avg = avg / ar.length;
        // print all 
        System.out.println("Array: " + Arrays.toString(ar));
        System.out.println("Max: " + Double.toString(max));
        System.out.println("Min: " + Double.toString(min));
        System.out.println("Aversge: " + Double.toString(avg));
    }
}
