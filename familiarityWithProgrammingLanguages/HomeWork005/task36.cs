namespace MyApp;

public class Task36{

//Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
//[3, 7, 23, 12] -> 19
//[-4, -6, 89, 6] -> 0
    public static void Do(){
        Console.Write("Input size of array: ");
        int array_size = Convert.ToInt32(Console.ReadLine());
        int[] array = new int [array_size];
        for (int i = 0; i < array.Length; i++){ array[i] = new Random().Next(); } 
    
        int oddSum = 0;
        for (int i = 1; i < array.Length; i = i + 2){ oddSum += array[i]; }
    
        Console.WriteLine("Array: [{0}]", string.Join(", ", array));
        Console.WriteLine($"Sum of elements in odd positions equal {oddSum}.");
}
}