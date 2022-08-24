package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	flagData, _ := ioutil.ReadFile("/flag")
	fmt.Println(string(flagData))
}
