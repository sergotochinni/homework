namespace MyApp{
    public class MyClass{

        public static void printArray(string[] array){
            Console.WriteLine("Array: [\"{0}\"]", string.Join("\", \"", array));
            return;
        }

        public static void Main(string[] args){
            string[] exampleArray = new string[4]{"hello", "2", "world", ":-)"};
//            string[] exampleArray = {"1234", "1567", "-2", "computer science"};
//            string[] exampleArray = {"Russia", "Denmark", "Kazan"};
            string[] mainArray;
            int lenOfArray;

            Console.Write("Input the number of array elements of press 'Enter' to use a test array: ");
            string line = Console.ReadLine();
            if (line == "") {
                lenOfArray = exampleArray.Length;
                mainArray = new string[lenOfArray];
                exampleArray.CopyTo(mainArray, 0);
            } else {
                lenOfArray = Convert.ToInt32(line);
                mainArray = new string[lenOfArray];
                for (int i=0; i<lenOfArray; i++){
                    Console.Write("Input {0} element: ", i);
                    mainArray[i] = Console.ReadLine();
                }
            }

            printArray(mainArray);

//            string[] resultArray;

        }
    }
}
