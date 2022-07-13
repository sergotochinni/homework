namespace MyApp;

public class Task38{

//Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
//[3 7 22 2 78] -> 76
public static void Do(){
    Console.Write("Input size of array: ");
    int array_size = Convert.ToInt32(Console.ReadLine());
    double[] array = new double[array_size];
    for (int i = 0; i < array.Length; i++){
        array[i] = new Random().NextDouble();
    } 
    double max = array[0];
    double min = array[0];
    for (int i = 0; i < array.Length; i++){
        if (array[i] < min){
            min = array[i];
        }else if (array[i] > max){
            max = array[i];
        }
    }
    Console.WriteLine("Array: [{0}]", string.Join(", ", array));
    Console.WriteLine($"Max - Min = {max-min}.");
}
}