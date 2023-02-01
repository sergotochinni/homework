package Programmer.familiarityWithJava.homeWork4;

import java.util.ArrayDeque;
import java.util.Deque;

public class task3 {

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
        String[] stroki = {"()[]", "()", "{[()]}", "()()", ")()(}", "{([{]})}"};
        for(String item: stroki){
            System.out.println(item + " = " + validate(item));;
        }
    }
    
    public static boolean validate(String str){
        Deque<Character> dq = new ArrayDeque<>();
        for(int i = 0; i < str.length(); i++){
            char elem = str.charAt(i);
            if ("[{(".indexOf(elem) >= 0){
                dq.addFirst(elem);
            } else {
                if (dq.peekFirst() == null) return false;
                char stack = dq.pollFirst();
                if (elem == ')' && stack != '(') return false;
                if (elem == '}' && stack != '{') return false;
                if (elem == ']' && stack != '[') return false;
            }
        }
        if (dq.size() != 0) return false;
        return true;
        }
    }
    