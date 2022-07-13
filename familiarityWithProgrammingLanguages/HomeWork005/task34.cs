namespace MyApp;

public class Task34{

//Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
//[345, 897, 568, 234] -> 2
public static void Do(){
    Console.Write("Input size of array: ");
    int array_size = Convert.ToInt32(Console.ReadLine());
    int[] array = new int [array_size];
    for (int i = 0; i < array.Length; i++){
        array[i] = new Random().Next(100, 999);
    } 
    int count = 0;
    for (int i = 0; i < array.Length; i++){
        if (array[i] % 2 == 0) count++;
    }
    Console.WriteLine("Array: [{0}]", string.Join(", ", array));
    Console.WriteLine($"In array {count} even numbers.");
}
}