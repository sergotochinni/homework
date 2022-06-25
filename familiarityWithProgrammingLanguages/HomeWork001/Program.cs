Console.WriteLine("Задача 2: программа, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.");
//a = 5; b = 7 -> max = 7
//a = 2 b = 10 -> max = 10
//a = -9 b = -3 -> max = -3
Console.Write("Input first number: ");
int num1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Input second number: ");
int num2 = Convert.ToInt32(Console.ReadLine());

if (num1 == num2){
    Console.WriteLine("The numbers are equals.");
}
else{
    if (num1 > num2) {
        Console.Write("max = ");
        Console.Write(num1);
        Console.Write(", min = ");
        Console.WriteLine(num2);
    }
    else {
        Console.Write("max = ");
        Console.Write(num2);
        Console.Write(", min = ");
        Console.WriteLine(num1);
    }
}

Console.WriteLine();
Console.WriteLine("Задача 4: программа, которая принимает на вход три числа и выдаёт максимальное из этих чисел.");
//2, 3, 7 -> 7
//44 5 78 -> 78
//22 3 9 -> 22
Console.Write("Input first number: ");
num1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Input second number: ");
num2 = Convert.ToInt32(Console.ReadLine());

Console.Write("Input third number: ");
int num3 = Convert.ToInt32(Console.ReadLine());

int max = num1;
if (num2 > max) {
    max = num2;
}
if (num3 > max) {
    max = num3;
}

Console.Write("max = ");
Console.WriteLine(max);


Console.WriteLine();
Console.WriteLine("Задача 6: программа, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).");
//4 -> да
//-3 -> нет
//7 -> нет
Console.Write("Input number: ");
num1 = Convert.ToInt32(Console.ReadLine());
if (num1 % 2 == 0) {
    Console.WriteLine("Number is even.");
}
else {
    Console.WriteLine("Number is odd.");
}


Console.WriteLine();
Console.WriteLine("Задача 8: программа, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.");
//5 -> 2, 4
//8 -> 2, 4, 6, 8
Console.Write("Input number: ");
num1 = Convert.ToInt32(Console.ReadLine());

int i = 2;
while (i <= num1) {
    Console.Write(i);
    Console.Write(" ");
    i = i + 2;
}
Console.WriteLine();
