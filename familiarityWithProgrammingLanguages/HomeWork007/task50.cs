namespace MyApp{

    public class Task50{

        public static void Do(){
// Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 17 -> такого числа в массиве нет
            Console.Write("Inpun m: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Write("Inpun n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[,] arr = MyClass.CreateTwoDimensionalArray(m, n, 0, 1000);
            MyClass.PrintTwoDimensionalArray(arr);                        
            Console.Write($"Inpun number of row (1..{m}): ");
            int row = Convert.ToInt32(Console.ReadLine());
            Console.Write($"Inpun number of column (1..{n}): ");
            int column = Convert.ToInt32(Console.ReadLine());
            try
            {
                Console.WriteLine(arr[row-1, column-1]);
            }
            catch{
                Console.WriteLine("Element not found.");
            }
        }
    }
}