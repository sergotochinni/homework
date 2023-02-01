Основной зал - задача 2. Задача 3 по желанию.
Зал1,Зал3 - Задача 3 и HomeWork
Зал2 - Задача 2 и Задача3. HomeWork - по желанию
Кто не был на семинаре - Задача 1, Задача 2 - остальное по желанию.

Задачи дублирую -->

public class Task1 {

// Дан Deque состоящий из последовательности цифр.
// Необходимо проверить, что последовательность цифр является палиндромом
public static void main(String[] args) {
    Deque<Integer> deque = new ArrayDeque<>(Arrays.asList(1,2,3,4,5,6));

}


public boolean checkOn(Deque<Integer> deque){

    return false;
}

}

public class Task2 {

//Даны два Deque представляющие два неотрицательных целых числа. Цифры хранятся в обратном порядке,
// и каждый из их узлов содержит одну цифру.
// Сложите два числа и верните сумму в виде связанного списка.
public static void main(String[] args) {
    Deque<Integer> d1 = new ArrayDeque<>(Arrays.asList(1,2,3));
    Deque<Integer> d2 = new ArrayDeque<>(Arrays.asList(5,4,7));
    // result [6,6,0,1]

}


public Deque<Integer> sum(Deque<Integer> d1, Deque<Integer> d2) {

    return new ArrayDeque<>();
}

}

public class Task3 {

//Дана строка содержащая только символы '(', ')', '{', '}', '[' и ']', определите,
// является ли входная строка логически правильной.
// Входная строка логически правильная, если:
// 1) Открытые скобки должны быть закрыты скобками того же типа.
// 2) Открытые скобки должны быть закрыты в правильном порядке. Каждая закрывающая скобка имеет соответствующую
// открытую скобку того же типа.
// ()[] = true
// () = true
// {[()]} = true
// ()() = true
// )()( = false

public static void main(String[] args) {

}

public boolean validate(Deque<Integer> deque){

    return false;
}

}

public class Homework {

//Даны два Deque представляющие два целых числа. Цифры хранятся в обратном порядке,
// и каждый из их узлов содержит одну цифру.
public static void main(String[] args) {
    Homework hw = new Homework();
    hw.multiple(new ArrayDeque<>(Arrays.asList(5,2)), new ArrayDeque<>(Arrays.asList(4)));
    // result [0,0,1]
    hw.sum(new ArrayDeque<>(Arrays.asList(5,-2)), new ArrayDeque<>(Arrays.asList(5)));
    // result [0,-2]
}

// Умножьте два числа и верните произведение в виде связанного списка.
public Deque<Integer> multiple(Deque<Integer> d1, Deque<Integer> d2){

    return new ArrayDeque<>();
}

// Сложите два числа и верните сумму в виде связанного списка. Одно или два числа должны быть отрицательными
public Deque<Integer> sum(Deque<Integer> d1, Deque<Integer> d2){

    return new ArrayDeque<>();
}

}
