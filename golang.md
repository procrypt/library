#### Insert quotes inside a format string eg., Print "Hello"

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
