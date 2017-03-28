#### Insert quotes inside a format string eg., Print "Hello"

using `%q` a double-quoted string safely escaped with Go syntax.
```golang
package main
import "fmt"

func main() {
    var i = "Hello"
    fmt.Printf("%q", i)
}

$ go run hello.go
"Hello"
```
