namespace MyApp;

public class Task41{
//Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
//0, 7, 8, -2, -2 -> 2
//1, -7, 567, 89, 223-> 3
public static int Do(int m){
    int count = 0;
    for (int i=0; i<m; i++){
        Console.Write($"Input number {i+1}: ");
        if (Convert.ToInt32(Console.ReadLine()) > 0) {
            count++;
        }
    }
    return count;
}

}