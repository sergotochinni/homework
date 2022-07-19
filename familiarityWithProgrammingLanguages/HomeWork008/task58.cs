namespace MyApp{

    public class Task58{

        public static void Do(){
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
            int[,] arr1 = MyClass.CreateTwoDimensionalArray(5, 8, 0, 10);
            Console.Write("First ");
            MyClass.PrintTwoDimensionalArray(arr1);
            int rows = arr1.GetLength(0);
            int columns = arr1.GetLength(1);
            int[,] arr2 = MyClass.CreateTwoDimensionalArray(rows, columns, 0, 10);
            Console.Write("Second ");
            MyClass.PrintTwoDimensionalArray(arr2);
            int[,] result = new int[rows, columns];
            //for every row
            for (int i = 0; i < rows; i++){
                for (int j = 0; j < columns; j++){
                    result[i,j] = arr1[i,j] * arr2[i,j];
                }
            }
            Console.Write("First Array * Second Array = ");
            MyClass.PrintTwoDimensionalArray(result);
        }
    }
}