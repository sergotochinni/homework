namespace MyApp;

public class Task43{
//Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
//b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; 5,5)
public static double[] Do(double b1, double k1, double b2, double k2){
    //double[] m = new double[2];
    double x = (b2 - b1) / (k1 - k2);
    double y = k1 * x + b1;
    return new double[]{x, y};
}



}