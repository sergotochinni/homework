namespace MyApp;

public class MainClass{


public static void Main(string[] args){
Console.WriteLine("Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.");
Task34.Do();
Console.WriteLine();

Console.WriteLine("Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.");
Task36.Do();
Console.WriteLine();


Console.WriteLine("Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.");
Task38.Do();
Console.WriteLine();


Console.WriteLine("Задача 19: Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.");
Console.Write("Input number: ");
Console.WriteLine($"Is palindrom? - {Task19.Do(Convert.ToInt32(Console.ReadLine()))}");
Console.WriteLine();

}
}