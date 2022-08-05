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
/*
Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
1 2 4 7
2 3 5 9
2 4 4 8
*/
            Console.WriteLine("Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.");
            Task54.Do();
            Console.WriteLine();

/*
Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7
Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка
*/
            Console.WriteLine("Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.");
            Task56.Do();
            Console.WriteLine();

/*
Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Например, заданы 2 массива:
1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7
и
1 5 8 5
4 9 4 2
7 2 2 6
2 3 4 7
Их произведение будет равно следующему массиву:
1 20 56 10
20 81 8 6
56 8 4 24
10 6 24 49
*/
            Console.WriteLine("Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.");
            Task58.Do();
            Console.WriteLine();

/*
Задача 60. Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
массив размером 2 x 2 x 2
12(0,0,0) 22(0,0,1)
45(1,0,0) 53(1,0,1)
*/
            Console.WriteLine("Задача 60. Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.");
            Task60.Do();
            Console.WriteLine();

/*
Задача 62. Заполните спирально массив 4 на 4.
Например, на выходе получается вот такой массив:
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
*/
            Console.WriteLine("Задача 62. Заполните спирально массив m на n.");
            Task62.Do();
            Console.WriteLine();

        }
    }
}






