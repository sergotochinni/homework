package Programmer.familiarityWithJava.tasksFromLections;

import java.util.Random;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;

public class task1 {
    /*
     * 1. Задана натуральная степень k. Сформировать случайным
     * образом список коэффициентов (значения от 0 до 100)
     * многочлена многочлен степени k.
     */
    public static void main(String[] args) {

        Scanner iScanner = new Scanner(System.in);
        System.out.print("Enter power: ");
        int k = iScanner.nextInt();
        iScanner.close();

        String s = "";
        Random gen = new Random();;

        for (int i = k; i >=0; i--){
            int a = gen.nextInt(100);
            if (a != 0) {
                s = s + (i == k ? "":(gen.nextBoolean() ? "-":"+")) + (a == 1 ? "":Integer.toString(a)) + (i == 0 ? "":"x" + (i == 1 ? "": "^" + Integer.toString(i)));
            }
        }
        s = s + " = 0";

        System.out.println(s);

        try (FileWriter file = new FileWriter("polinom.txt", false)) {
            file.write(s + "\n");
            file.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
        
    }       
}
