namespace MyApp{
    public class MyClass{
        public static void Main(string[] args){
            Console.Write("Input number of elements: ");
            int elems = Convert.ToInt32(Console.ReadLine());
            int[] array = new int[elems];
            for (int i = 0; i < elems; i++){
                Console.Write("Input {0} element: ", i);
                array[i] = Convert.ToInt32(Console.ReadLine());
            }
            Console.Write("Input shift: ");
            int shift = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Array: [{0}]", string.Join(", ", array));

            int[] shifted = new int[elems];
            shift = shift % elems;
            for (int i = 0; i < elems; i++){
                shifted[(i + shift + elems) % elems] = array[i];
            }

            Console.WriteLine("Array: [{0}]", string.Join(", ", shifted));

        }
    }
}
