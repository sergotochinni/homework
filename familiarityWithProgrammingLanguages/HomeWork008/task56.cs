namespace MyApp{

    public class Task56{

        public static void Do(){
/*
Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7
Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка
*/
            int[,] arr = MyClass.CreateTwoDimensionalArray(5, 8, 0, 10);
            MyClass.PrintTwoDimensionalArray(arr);
            int rows = arr.GetLength(0);
            int columns = arr.GetLength(1);
            int min = 0;
            //first row summ
            for (int j = 0; j < columns; j++){
                min += arr[0,j];
            }
            int minrow = 0;
            //for every row
            for (int i = 0; i < rows; i++){
                int sum = 0;
                for (int j = 0; j < columns; j++){
                    sum += arr[i,j];
                }
                if (sum < min) {
                    min = sum;
                    minrow = i;
                }
            }
            Console.WriteLine("Number of row with min summ of elements eq {0}", minrow);
        }
    }
}