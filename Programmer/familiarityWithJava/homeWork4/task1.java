package Programmer.familiarityWithJava.homeWork4;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class task1 {
        // Дан Deque состоящий из последовательности цифр.
        // Необходимо проверить, что последовательность цифр является палиндромом
        public static void main(String[] args) {
            Deque<Integer> deque = new ArrayDeque<>(Arrays.asList(1,2,3,4,5,6));
            System.out.println(deque + " is " + (checkOn(deque) ? "":"not ") + "palindrom.");
            deque = new ArrayDeque<>(Arrays.asList(1,2,3,4,5,6,5,4,3,2,1));
            System.out.println(deque + " is " + (checkOn(deque) ? "":"not ") + "palindrom.");
        }
        
        
        public static boolean checkOn(Deque<Integer> deque){
            while(deque.size()>1){
                if (deque.pollFirst() != deque.pollLast()) return false;
            }
            return true;
        }
        
}
