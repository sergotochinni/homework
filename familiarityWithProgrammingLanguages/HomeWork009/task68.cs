namespace MyApp{

    public class Task68{
        public static int AkkermanNumbers(int m, int n){
            if (m == 0) { return n+1;}
            if (m >0 && n==0) { return AkkermanNumbers(m-1, 1);}
            return AkkermanNumbers(m-1, AkkermanNumbers(m, n-1));
        }
// Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
// m = 2, n = 3 -> A(m,n) = 29
        public static void Do(){
            Console.Write("Input m: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Write("Input n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"Akkerman({m}, {n}) eq {AkkermanNumbers(m, n)}");                
        }
    }
}