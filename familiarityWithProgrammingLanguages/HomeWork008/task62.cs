namespace MyApp{

    public class Task62{

        public static void Do(){
/*
Задача 62. Заполните спирально массив m на n.
Например, на выходе получается вот такой массив:
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
*/
            Console.Write("Inpun m: ");
            int rows = Convert.ToInt32(Console.ReadLine());
            Console.Write("Inpun n: ");
            int columns = Convert.ToInt32(Console.ReadLine());
            int[,] arr = new int[rows, columns];
            int limDown = rows-1;
            int limRight = columns-1;
            int limTop = 0;
            int limLeft = 0;
            int x = 0;
            int y = 0;
            int dx = 0;
            int dy = 1;
            for (int i = 1; i <= rows*columns; i++){
                arr[x,y] = i;
                if (dx == 1 && x == limDown){
                    dx = 0;
                    dy = -1;
                    limRight--;
                }
                if (dx == -1 && x == limTop){
                    dx = 0;
                    dy = 1;
                    limLeft++;
                }
                if (dy == 1 && y == limRight){
                    dx = 1;
                    dy = 0;
                    limTop ++;
                }
                if (dy == -1 && y == limLeft){
                    dx = -1;
                    dy = 0;
                    limDown--;
                }
                x += dx;
                y += dy;
            }//end for
            MyClass.PrintTwoDimensionalArray(arr);
        }
    }
}
