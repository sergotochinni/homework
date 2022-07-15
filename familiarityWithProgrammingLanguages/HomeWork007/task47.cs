namespace MyApp{

    public class Task47{

        public static void Do(){
// Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
// m = 3, n = 4.
// 0,5 7 -2 -0,2
// 1 -3,3 8 -9,9
// 8 7,8 -7,1 9
            Console.Write("Inpun m: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Write("Inpun n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            double[,] arr = MyClass.CreateTwoDimensionalArray(m, n, -10000, 10000, 2);
            MyClass.PrintTwoDimensionalArray(arr);
        }
    }
}