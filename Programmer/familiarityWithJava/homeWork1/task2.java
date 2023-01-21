package Programmer.familiarityWithJava.homeWork1;

import java.util.Arrays;
import java.util.Scanner;

public class task2 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter the length of array: ");
        int ln = scn.nextInt();
        scn.close();
        long[] ar = new long[ln];
        for (int i = 0; i < ln; i++){
            ar[i] = Math.round(Math.random()*1000);
        }

        System.out.println(("Source array: " + Arrays.toString(ar)));

        long tmp = 0;
        // bubble sort
        for (int i = ar.length-1; i > 0; i--){
            for (int j = 0; j < i; j++){
                if (ar[j] > ar[j+1]) {
                    tmp = ar[j];
                    ar[j] = ar[j+1];
                    ar[j+1] = tmp;
                }
            }
        }
        System.out.println(("Sorted array: " + Arrays.toString(ar)));
        
    }
}
