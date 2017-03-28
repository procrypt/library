#### Insert quotes inside a format string eg., Print "Hello"

using `%q` a double-quoted string and a single-quoted character literal is safely escaped with Go syntax.
```golang
package main
import "fmt"

func main() {
    fmt.Printf("%q", "Hello")
    fmt.Printf("%q", "2")
}

$ go run hello.go
"Hello"
"2"
```
