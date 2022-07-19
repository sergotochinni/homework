namespace MyApp{

    public class Task54{

        public static void Do(){
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
            int[,] arr = MyClass.CreateTwoDimensionalArray(5, 8, 0, 100);
            MyClass.PrintTwoDimensionalArray(arr);
            int rows = arr.GetLength(0);
            int columns = arr.GetLength(1);
            //for every row
            for (int i = 0; i < rows; i++){
                //exchange sort
                for (int j = columns - 1; j > 0; j--){
                    for (int k = 0; k < j; k++){
                        if (arr[i,k] > arr[i,k+1]) {
                            int tmp = arr[i,k];
                            arr[i,k] = arr[i,k+1];
                            arr[i,k+1] = tmp;
                        }
                    }
                }
            }
            Console.Write("Sorted ");
            MyClass.PrintTwoDimensionalArray(arr);

        }
    }
}
