namespace MyApp{

//    public static class ArrayExtensions{
//        public static IEnumerable<T> GetRow<T>(this T[,] array, int rowIndex){
//            int columnsCount = array.GetLength(1);
//            for (int colIndex = 0; colIndex < columnsCount; colIndex++)
//                yield return array[rowIndex, colIndex];
//            }
//    }

    public class MyClass{

        public static double[,] CreateTwoDimensionalArray(int m, int n, int min, int max, int precision){
            double[,] array = new double[m, n];
            for (int i = 0; i < m; i++){
                for (int j = 0; j < n; j++){
                    array[i,j] = Math.Round(new Random().NextDouble(), precision) + Convert.ToDouble(new Random().Next(min, max));
                }
            }
            return array;
        }

        public static int[,] CreateTwoDimensionalArray(int m, int n, int min, int max){
            int[,] array = new int[m,n];
            for (int i = 0; i < m; i++){
                for (int j = 0; j < n; j++){
                    array[i,j] = new Random().Next(min, max);
                }
            }
            return array;
        }

//        public static void PrintTwoDimensionalArray<T>(T[,] array){
//            for (int i = 0; i < array.GetLength(0); i++){
//                Console.WriteLine("{0}", String.Join(", ", array.GetRow(i)));
//            }
//        }
        public static void PrintTwoDimensionalArray<T>(T[,] array){
            int rows = array.GetLength(0);
            int columns = array.GetLength(1);
            Console.WriteLine("Array {0} x {1}:", rows, columns);
            string [] sArr = new string [columns];
            for (int i = 0; i < rows; i++){
                for (int j = 0; j < columns; j++){
                    sArr[j] = String.Format("{0,10}", array[i,j]);
                }
                Console.WriteLine("{0}", String.Join(", ", sArr));
            }
        }
        public static void Main(string[] args){
// Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
// m = 3, n = 4.
// 0,5 7 -2 -0,2
// 1 -3,3 8 -9,9
// 8 7,8 -7,1 9
            Console.WriteLine("Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.");
            Task47.Do();
            Console.WriteLine();

// Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 17 -> такого числа в массиве нет

            Console.WriteLine("Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.");
            Task50.Do();
            Console.WriteLine();

// Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.
            Console.WriteLine("Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.");
            Task52.Do();
            Console.WriteLine();

        }
    }
}
