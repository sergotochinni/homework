package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func printArray(array []string) {
	fmt.Printf("Array: " + strings.ReplaceAll(fmt.Sprintf("%+q", array), "\" \"", "\", \"") + "\n")

}

func append(array []string, value string) []string {
	result := make([]string, len(array)+1)
	copy(result, array)
	result[len(array)] = value
	return result
}

func main() {
	var (
		mainArray  []string
		lenOfArray int
	)

	exampleArray := []string{"hello", "2", "world", ":-)"}
	//exampleArray := []string{"1234", "1567", "-2", "computer science"}
	//exampleArray := []string{"Russia", "Denmark", "Kazan"}

	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Input the number of array elements of press 'Enter' to use a test array: ")

	scanner.Scan()
	text := scanner.Text()

	if len(text) == 0 {
		lenOfArray = len(exampleArray)
		mainArray = make([]string, lenOfArray)
		copy(mainArray, exampleArray)
	} else {
		lenOfArray, err := strconv.Atoi(text)
		if err != nil {
			os.Exit(1)
		}
		mainArray = make([]string, lenOfArray)
		for i := 0; i < lenOfArray; i++ {
			fmt.Printf("Input %d element: ", i)
			scanner.Scan()
			mainArray[i] = scanner.Text()
		}
	}

	printArray(mainArray)

	resultArray := make([]string, 0)

	for i := 0; i < lenOfArray; i++ {
		if len(mainArray[i]) <= 3 {
			resultArray = append(resultArray, mainArray[i])
		}
	}

	printArray(resultArray)
}
