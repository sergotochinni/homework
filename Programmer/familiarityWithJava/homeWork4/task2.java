package Programmer.familiarityWithJava.homeWork4;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class task2 {
        //Даны два Deque представляющие два неотрицательных целых числа. Цифры хранятся в обратном порядке,
        // и каждый из их узлов содержит одну цифру.
        // Сложите два числа и верните сумму в виде связанного списка.
        public static void main(String[] args) {
//            Deque<Integer> d1 = new ArrayDeque<>(Arrays.asList(1,2,3));
//            Deque<Integer> d2 = new ArrayDeque<>(Arrays.asList(5,4,7));
            Deque<Integer> d1 = new ArrayDeque<>(Arrays.asList(1,2,3));
            Deque<Integer> d2 = new ArrayDeque<>(Arrays.asList(5,4,7,9,0,2));
            System.out.println(d1);
            System.out.println("+");
            System.out.println(d2);
            System.out.println("result\n" + sum(d1, d2));
        
        }
        public static Deque<Integer> sum(Deque<Integer> d1, Deque<Integer> d2) {
            Deque<Integer> d3 = new ArrayDeque<>();
            Integer summ = 0;
            Integer carry = 0;
            while(d1.size() != 0 || d2.size() != 0){
                summ = 0;
                if (d1.peekFirst() != null) summ += d1.pollFirst();
                if (d2.peekFirst() != null) summ += d2.pollFirst();
                summ += carry;
                carry = summ / 10;
                summ %= 10;
                d3.addLast(summ);
            }
            if (carry == 1) d3.addLast(carry);
            return d3;
        }
}
