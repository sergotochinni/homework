Console.WriteLine("Задача 10: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.");
//456 -> 5
//782 -> 8
//918 -> 1
Console.Write("Input number: ");
int num = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"the second digit is {num / 10 % 10}");


Console.WriteLine();
Console.WriteLine("Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.");
//645 -> 5
//78 -> третьей цифры нет
//32679 -> 6
Console.Write("Input number: ");
num = Convert.ToInt32(Console.ReadLine());
int res = num / 10 / 10 % 10;
if (res == 0){
    Console.WriteLine("the third digit is missing.");
} else {
    Console.WriteLine($"the third digit is {res}");
}


Console.WriteLine();
Console.WriteLine("Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.");
//6 -> да
//7 -> да
//1 -> нет
Console.Write("Input number: ");
num = Convert.ToInt32(Console.ReadLine());
if (num == 6 || num == 7){
    Console.WriteLine("Yes");
} else {
    Console.WriteLine("No");
}