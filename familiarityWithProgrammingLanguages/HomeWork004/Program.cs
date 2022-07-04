//Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
//3, 5 -> 243 (3⁵)
//2, 4 -> 16
int task25(int a, int b){
    int result = 1;
    for (int i = 1; i <= b; i++){
        result = result * a;
    }
    return result;
}


//Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
//452 -> 11
//82 -> 10
//9012 -> 12
int task27(int num){
    int result = 0;
    while (num > 0) {
        result = result + (num % 10);
        num = num / 10;
    }
    return result;
}


//Задача 29: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
//1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]
//6, 1, 33 -> [6, 1, 33]
void task29(){
    int[] arr = new int[8];
    for (int i = 0; i < arr.Length; i++){
        arr[i] = new Random().Next(1,100);
    }
    Console.WriteLine("[{0}]", string.Join(", ", arr));
}

Console.WriteLine("Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.");
Console.Write("Input number: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.Write("Input pow: ");
int b = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"{a} in pow {b} equal {task25(a, b)}");
Console.WriteLine();

Console.WriteLine("Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.");
Console.Write("Input number: ");
int c = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"Sum of all digits of {c} equal {task27(c)}");
Console.WriteLine();

Console.WriteLine("Задача 29: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.");
task29();
Console.WriteLine();
