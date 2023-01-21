package Programmer.familiarityWithJava.tasksFromLections;

import java.io.BufferedReader;
import java.io.FileReader;

public class task2 {
    /* 2. Даны два файла, в каждом из которых находится запись многочлена.
    * Сформировать файл содержащий сумму многочленов.
    */
    public static int[] arr;
    public static void main(String[] args) throws Exception{
        BufferedReader br1 = new BufferedReader(new FileReader("polinom1.txt"));
        BufferedReader br2 = new BufferedReader(new FileReader("polinom2.txt"));
        String pol1 = br1.readLine();
        String pol2 = br2.readLine();
        br1.close();
        br2.close();
        int[] arr1;
        int[] arr2;
        arr1 = parsePolinom(pol1);
        arr2 = parsePolinom(pol2);

        System.out.println(pol1);
        System.out.println("+");
        System.out.println(pol2);
        System.out.println("=");

        int max = arr1.length;
        if (max < arr2.length) max = arr2.length;
        int[] arr_res = new int[max];
        for (int i = 0; i < max; i++){
            arr_res[i] = (i < arr1.length ? arr1[i]:0) + (i < arr2.length ? arr2[i]:0);
        }

        String s = "";

        for (int i = arr_res.length-1; i >=0; i--){
            int a = arr_res[i];
            if (a != 0) {
                s = s + (a < 0 ? "":(i == arr_res.length-1 ? "":"+")) + (a == 1 ? "":Integer.toString(a)) + (i == 0 ? "":"x" + (i == 1 ? "": "^" + Integer.toString(i)));
            }
        }
        s = s + " = 0";    
        System.out.println(s);    
}

public static int[] parsePolinom(String pol) {
    boolean first_k = true;
    String k = "";
    int n = 0;
    int pow = 0;
    int sign = 1;
    for (int i = 0; i < pol.length(); i++){
        switch (pol.charAt(i)){
            case '0':
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                k = k + pol.charAt(i);
                break;
            case 'x':
                n = Integer.parseInt(k) * sign;
                k = "";
                break;
            case '+':
                sign = 1;
                pow = (k == "" ? 1:Integer.parseInt(k));
                k = "";
                if (first_k) {
                    first_k = false;
                    arr = new int[pow+1];
                    for (int j = 0; j < arr.length; j++) arr[j] = 0;
                }
                arr[pow] = n;
                pow = 0;
                n = 0;
                break;
            case '-':
                sign = -1;
                pow = (k == "" ? 1:Integer.parseInt(k));
                k = "";
                if (first_k) {
                    first_k = false;
                    arr = new int[pow+1];
                    for (int j = 0; j < arr.length; j++) arr[j] = 0;
                }
                arr[pow] = n;
                pow = 0;
                n = 0;
                break;
            case '^':
                break;
            case ' ':
                break;
            case '=':
                pow = Integer.parseInt(k);
                if (n != 0){
                    arr[pow] = n;
                } else {
                    arr [0] = pow;
                }
                break;
            default:
                break;
        }
    }
    return arr;
    }
}