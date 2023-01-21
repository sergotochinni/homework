package Programmer.familiarityWithJava.tasksFromLections;

public class task1seminar {
    public static void main(String[] args) {
        int incounter = 0;
        int rescounter = 0;
        int i = 0;
        int[] arr = new int[] {1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1}; 
        while (i < arr.length){
            if (arr[i] == 1){
                incounter++;
            }
            if (arr[i] != 1 || i == arr.length-1){
                if (incounter > rescounter){
                    rescounter = incounter;
                    incounter = 0;
                }
            }
            i++;
        }
        System.out.println(rescounter);
    }
}
