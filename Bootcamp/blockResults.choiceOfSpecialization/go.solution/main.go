package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Simple Shell")
	fmt.Println("---------------------")

	for {
		fmt.Print("-> ")
		scanner.Scan()
		text := scanner.Text()

		if len(text) != 0 {
			fmt.Println("hello, ", text)
		} else {
			break
		}

	}
}
