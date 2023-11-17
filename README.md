

## Overview

Briefly describe the purpose and functionality of your Python project that implements data structures and algorithms.
```
@dataclass
class LinkedList[T]:
    head: Node[T] | None = None
    tail: Node[T] | None = None

    def push(self, value: T) -> None:
        ...
```
- Data Structures and algorithms
- Type hint with new generic type system, 
- require python >= 3.12
