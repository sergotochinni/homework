namespace MyApp{

    public class Task66{

        public static int SumNumbers(int m, int n){
            if (m == n) {return m; }
            return m+SumNumbers(m+1, n);
        }
// Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30
        public static void Do(){
            Console.Write("Input m: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Write("Input n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"Sum of all numbers eq {SumNumbers(m, n)}");            
        }
    }
}