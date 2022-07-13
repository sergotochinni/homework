//Задача 19: Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
string task19(int num){
//    Console.WriteLine("Задача 19: Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.");
//14212 -> нет
//12821 -> да
//23432 -> да
    string dig = Convert.ToString(num);
    for (int i = 0; i < dig.Length / 2; i++){
        if (dig[i] != dig[dig.Length-1-i]) return "No";
    }
    return "Yes";
}

//Задача 21: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
double task21(int[] a, int[] b){
//    Console.WriteLine("Задача 21: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.");
//A (3,6,8); B (2,1,-7), -> 15.84
//A (7,-5, 0); B (1,-1,9) -> 11.53
Console.WriteLine(a);
Console.WriteLine(b);
    double result = Math.Sqrt(Math.Pow((a[2] - b[2]), 2) + Math.Pow((a[1] - b[1]), 2) + Math.Pow((a[0] - b[0]), 2));
    return result;
}


//Задача 23: Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
void task23(int num){
//3 -> 1, 8, 27
//5 -> 1, 8, 27, 64, 125
    Console.Write("1");
    for (int i = 2; i <= num; i++){
        Console.Write($", {i*i*i}");
    }
    Console.WriteLine();
}

Console.WriteLine("Задача 19: Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.");
Console.Write("Input number: ");
Console.WriteLine($"Is palindrom? - {task19(Convert.ToInt32(Console.ReadLine()))}");
Console.WriteLine();

Console.WriteLine("Задача 21: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.");
int[] m1 = new int[3];
int[] m2 = new int[3];
Console.Write("Input x1: ");
m1[0] = Convert.ToInt32(Console.ReadLine());
Console.Write("Input y1: ");
m1[1] = Convert.ToInt32(Console.ReadLine());
Console.Write("Input z1: ");
m1[2] = Convert.ToInt32(Console.ReadLine());
Console.Write("Input x2: ");
m2[0] = Convert.ToInt32(Console.ReadLine());
Console.Write("Input y2: ");
m2[1] = Convert.ToInt32(Console.ReadLine());
Console.Write("Input z2: ");
m2[2] = Convert.ToInt32(Console.ReadLine());
Console.Write("Distance: ");
Console.WriteLine(task21(m1, m2));
Console.WriteLine();

Console.WriteLine("Задача 23: Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.");
Console.Write("Input number: ");
task23(Convert.ToInt32(Console.ReadLine()));
Console.WriteLine();