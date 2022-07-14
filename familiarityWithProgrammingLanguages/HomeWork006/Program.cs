namespace MyApp;

public class MyClass{
//Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
//0, 7, 8, -2, -2 -> 2
//1, -7, 567, 89, 223-> 3
    public static void Main(string[] args){
        
        Console.WriteLine("Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.");
        Console.Write("Input m: ");
        Console.WriteLine($"Count of numbers > 0 eq {Task41.Do(Convert.ToInt32(Console.ReadLine()))}");
        Console.WriteLine();

//Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
//b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; 5,5)
        double b1, k1, b2, k2;

        Console.WriteLine("Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.");
        Console.Write("Input b1 (default 2): ");
        string str = Console.ReadLine();
        if (str == "") { b1 = 2; } 
        else { b1 = Convert.ToDouble(str); }

        Console.Write("Input k1 (default 5): ");
        str = Console.ReadLine();
        if (str == "") { k1 = 5; } 
        else { k1 = Convert.ToDouble(str); }

        Console.Write("Input b2 (default 4): ");
        str = Console.ReadLine();
        if (str == "") { b2 = 4; } 
        else { b2 = Convert.ToDouble(str); }

        Console.Write("Input k2 (default 9): ");
        str = Console.ReadLine();
        if (str == "") { k2 = 9; } 
        else { k2 = Convert.ToDouble(str); }

        Console.WriteLine("Coordinates of crosspoint is ({0})", string.Join("; ", Task43.Do(b1, k1, b2, k2)));
    }
}
