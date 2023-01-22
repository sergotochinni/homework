package Programmer.familiarityWithJava.tasksFromLections;

public class temp {
    public static void main(String[] args) {
        String str = "abcdefg";
        int[] arr = new int[] {5, 4, 3, 6, 1, 2, 7};
        String res = "";
        for (int i=0; i < str.length(); i++){
            res += str.charAt(arr[i]-1);
        }
        System.out.println(str);
        System.out.println(res);

        res = "";
        char[] chr = str.toCharArray();
        char[] chr2 = new char[chr.length];
        System.out.println(chr);
        for (int i = 0; i < chr.length; i++){
            chr2[arr[i]-1] = chr[i];
        }
        System.out.println(chr2);
    }
}
