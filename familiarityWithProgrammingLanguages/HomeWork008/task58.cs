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
            Console.Write("First array. Inpun rows: ");
            int rows1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("First array. Inpun columns: ");
            int columns1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Second array. Inpun rows: ");
            int rows2 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Second array. Inpun columns: ");
            int columns2 = Convert.ToInt32(Console.ReadLine());
            if (columns1 != rows2) {
                Console.WriteLine("Product is undefined. n columns of first matrix must equal to n rows of second matrix");
                return;
            }
            int[,] arr1 = MyClass.CreateTwoDimensionalArray(rows1, columns1, 0, 10);
            Console.Write("First ");
            MyClass.PrintTwoDimensionalArray(arr1);
            int[,] arr2 = MyClass.CreateTwoDimensionalArray(rows2, columns2, 0, 10);
            Console.Write("Second ");
            MyClass.PrintTwoDimensionalArray(arr2);
            int[,] result = new int[rows1, columns2];
            for (int i = 0; i < rows1; i++){
                for (int j = 0; j < columns2; j++){
                    result[i,j] = 0;
                }
            }
            for (int i = 0; i < rows1; i++){
                for (int j = 0; j < columns2; j++){
                    for (int k = 0; k < columns1; k++){
                        result[i,j] += arr1[i,k] * arr2[k,j];
                    }
                }
            }
            Console.Write("First Array * Second Array = ");
            MyClass.PrintTwoDimensionalArray(result);
        }
    }
}