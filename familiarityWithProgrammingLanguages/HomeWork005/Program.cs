//Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
//[345, 897, 568, 234] -> 2
void task34(){
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

//Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
//[3, 7, 23, 12] -> 19
//[-4, -6, 89, 6] -> 0
void task36(){
    Console.Write("Input size of array: ");
    int array_size = Convert.ToInt32(Console.ReadLine());
    int[] array = new int [array_size];
    for (int i = 0; i < array.Length; i++){
        array[i] = new Random().Next();
    } 
    int oddSum = 0;
    for (int i = 1; i < array.Length; i = i + 2){
        oddSum += array[i];
    }
    Console.WriteLine("Array: [{0}]", string.Join(", ", array));
    Console.WriteLine($"Sum of elements in odd positions equal {oddSum}.");
}

//Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
//[3 7 22 2 78] -> 76
void task38(){
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



Console.WriteLine("Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.");
task34();
Console.WriteLine();

Console.WriteLine("Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.");
task36();
Console.WriteLine();

Console.WriteLine("Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.");
task38();
Console.WriteLine();
