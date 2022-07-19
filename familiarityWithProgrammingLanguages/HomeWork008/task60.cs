namespace MyApp{

    public class Task60{

        public static void Do(){
/*
Задача 60. Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
массив размером 2 x 2 x 2
12(0,0,0) 22(0,0,1)
45(1,0,0) 53(1,0,1)
*/
            int x = 3;
            int y = 3;
            int z = 3;
            int [,,] arr = new int[x,y,z];
            //list for all two-digits numbers
            List<int> TwoDigitNumbers = new List<int>(90);
            //fill list all two-digits numbers
            for (int i = 10; i < 100; i++) {TwoDigitNumbers.Add(i);}
            //fill three-dimension array non repeated two-digit numbers
            for (int i = 0; i < x; i++){
                for(int j = 0; j < y; j++){
                    for (int k = 0; k < z; k++){
                        //get random ingex
                        int idx = new Random().Next(0, TwoDigitNumbers.Count);
                        //get two-digit number
                        int m = TwoDigitNumbers[idx];
                        //set to array
                        arr[i,j,k] = m;
                        //del two-digit number from list for non repeat
                        TwoDigitNumbers.Remove(m);
                    }
                }
            }
            for (int i = 0; i < x; i++){
                for(int j = y-1; j >= 0; j--){
                    for (int k = 0; k < z; k++){
                        Console.Write($"{arr[i,j,k]}({i},{j},{k}) ");
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}