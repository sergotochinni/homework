Console.Write("Input your name: ");
string username = Console.ReadLine();
if(username.ToLower() == "masha")
{
    Console.WriteLine("Wow, it is Masha.");
}
else
{
    Console.Write("Hello, ");
    Console.WriteLine(username);
}