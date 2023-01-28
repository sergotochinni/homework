package Programmer.familiarityWithJava.homeWork3;

import java.util.*;

public class homeWork {

// Пусть дан произвольный список целых чисел
public static void main(String[] args) {
    List<Integer> list = new ArrayList<>(Arrays.asList(1, 9, 2, 6, 4, 3, 5, 7, 8, 0));
    System.out.println("Array: " + list);
    System.out.println("Min: " + getMin(list));
    System.out.println("Max: " + getMax(list));
    System.out.println("Avg: " + getAverage(list));
    System.out.println("Even removed array: " + removeEvenValue(list));
}

// Нужно удалить из него четные числа
public static List<Integer> removeEvenValue(List<Integer> list){
    Iterator<Integer> it = list.iterator();
    while(it.hasNext()){
        Integer number= it.next();
        if(number % 2 ==0){
            it.remove();
        }
    }
    return list;
//v3
/*
     list.removeIf(num -> num%2==0);
    return list;
 */
// v2
/*
    int i = 0;
    while (i < list.size()){
        if (list.get(i) % 2 == 0) {
            list.remove(i);
        } else {
            i++;
        }
    }
    return list;
*/
    // v1
/*
    List<Integer> tmp = new ArrayList<>();
    for (Integer item: list){
        if (item % 2 != 0) tmp.add(item);
    }
    return tmp;
*/
}

// Найти минимальное значение
public static Integer getMin(List<Integer> list){
    int min = list.get(0);
    for (Integer item: list){
        if (item < min) min = item;
    }
    return min;
}

// Найти максимальное значение
public static Integer getMax(List<Integer> list){
    int max = list.get(0);
    for (Integer item: list){
        if (item > max) max = item;
    }
    return max;
}

// Найти среднее значение
public static Integer getAverage(List<Integer> list){
    int sum = 0;
    for (Integer item: list) sum += item;
    return sum / list.size();
}

}
