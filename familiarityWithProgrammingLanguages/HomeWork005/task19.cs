namespace MyApp;

public class Task19{

//Задача 19: Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
public static string Do(int num){
//    Console.WriteLine("Задача 19: Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.");
//14212 -> нет
//12821 -> да
//23432 -> да
    int firstNum = num / 1000;
    int secondNum = (num % 10 * 10) + (num / 10 % 10);
    if (firstNum != secondNum) return "No";
    return "Yes";
}
}