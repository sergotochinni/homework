namespace MyApp{

    public class Task52{

// Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.
        public static void Do(){
            Console.Write("Inpun m: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Write("Inpun n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[,] arr = MyClass.CreateTwoDimensionalArray(m, n, 0, 1000);
            MyClass.PrintTwoDimensionalArray(arr);
            double[] avg = new double[m];      
            for (int i = 0; i < m; i++){
                for (int j = 0; j < n; j++){
                    avg[i] += arr[i, j];
                }
                avg[i] = Math.Round((avg[i] / n), 1);
            }      
            Console.WriteLine("Average of each row eq: {0}", String.Join("; ", avg));
        }

    }
}