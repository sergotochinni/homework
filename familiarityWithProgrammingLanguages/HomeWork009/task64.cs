namespace MyApp{

    public class Task64{

        public static string PrintNumbers(int m, int n){
            if (m == n) {return Convert.ToString(m); }
            return Convert.ToString(m)+", "+PrintNumbers(m+1, n);
        }
// Задача 64: Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.
// M = 1; N = 5. -> ""1, 2, 3, 4, 5""
// M = 4; N = 8. -> ""4, 6, 7, 8""
        public static void Do(){
            Console.Write("Input m: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Write("Input n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(PrintNumbers(m, n));
        }
    }
}