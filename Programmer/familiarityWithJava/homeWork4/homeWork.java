package Programmer.familiarityWithJava.homeWork4;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class homeWork {

    //Даны два Deque представляющие два целых числа. Цифры хранятся в обратном порядке,
    // и каждый из их узлов содержит одну цифру.
    public static void main(String[] args) {
        homeWork hw = new homeWork();
        System.out.println(hw.multiple(new ArrayDeque<>(Arrays.asList(5,2)), new ArrayDeque<>(Arrays.asList(4))));
        // result [0,0,1]
        System.out.println(hw.sum(new ArrayDeque<>(Arrays.asList(5,-2)), new ArrayDeque<>(Arrays.asList(5))));
        // result [0,-2]
        System.out.println(hw.sum(new ArrayDeque<>(Arrays.asList(9, -6)), new ArrayDeque<>(Arrays.asList(8, -6))));
    }
    
    // Умножьте два числа и верните произведение в виде связанного списка.
    public Deque<Integer> multiple(Deque<Integer> d1, Deque<Integer> d2){
        Deque<Integer> d3 = new ArrayDeque<>();
        Integer mul = 0;
        Integer s1 = 0;
        Integer s2 = 0;
        Integer m = 1;
        Integer sign = 1;
        while(d1.size() != 0 || d2.size() != 0){
            if (d1.peekFirst() != null) s1 += Math.abs(d1.pollFirst()) * m;
            if (d2.peekFirst() != null) s2 += Math.abs(d2.pollFirst()) * m;
            m *= 10;
        }
        mul = s1 * s2;
        if (mul < 1) sign = -1;
        while(Math.abs(mul) > 0){
            d3.addLast(Math.abs(mul) % 10);
            mul /= 10;
        }
        return d3;    
    }
    
    // Сложите два числа и верните сумму в виде связанного списка. Одно или два числа должны быть отрицательными
    public Deque<Integer> sum(Deque<Integer> d1, Deque<Integer> d2){
        Deque<Integer> d3 = new ArrayDeque<>();
        Integer summ = 0;
        Integer carry = 0;
        Integer sign1 = 1;
        if (d1.peekLast() < 0) sign1 = -1;
        Integer sign2 = 1;
        if (d2.peekLast() < 0) sign2 = -1;
        if (sign1 == sign2){
            while(d1.size() != 0 || d2.size() != 0){
                summ = carry;
                if (d1.peekFirst() != null) summ += Math.abs(d1.pollFirst()) * sign1;
                if (d2.peekFirst() != null) summ += Math.abs(d2.pollFirst()) * sign2;
                carry = summ / 10;
                d3.addLast(summ%10);
            }
            if (carry != 0) d3.addLast(carry);
        } else {
            Integer s1 = 0;
            Integer s2 = 0;
            Integer m = 1;
            while(d1.size() != 0 || d2.size() != 0){
                if (d1.peekFirst() != null) s1 += Math.abs(d1.pollFirst()) * m;
                if (d2.peekFirst() != null) s2 += Math.abs(d2.pollFirst()) * m;
                m *= 10;
            }
            s1 *= sign1;
            s2 *= sign2;
            summ = s1 + s2;
            Integer sign = 1;
            if (summ < 1) sign = -1;
            while(Math.abs(summ) > 0){
                d3.addLast(Math.abs(summ) % 10);
                summ /= 10;
            }
            d3.addLast(d3.pollLast() * sign);
        }
        return d3;
    }
    
}