

# Stack
===================

A Stack is a linear data structure. It stores items using the Last In, First Out (LIFO) method. Whenever a new element is added to a stack, it is added to the top of the stack, and the top element is always removed first from a stack. In this article, we’ll be looking at ways to implement and use the stack in Python.

For more background on the different types of data structures in Python, check out my previous article.

Table of Contents
* Stack: Introduction
* Uses of Stacks
* Implementing Stacks

## Conclusion
Stack: Introduction
A great analogy we can use is stacking a pile of books. We always keep a new book on top and remove the topmost book. Stacks are similar to queues in that they are linear collections of items, but they differ in the order in which they are accessed. Stacks are used in a variety of areas from Operating System Software, in Compilers and Language Parsing, and to implement other complex Data Structures like Trees and Graphs.

### Push Pop push in a stack is putting an item on top of the stack.

### pop in a stack is taking out the top item in the stack.

## Uses of Stacks
Stacks are used extensively in a lot of places.

### Compilers and Parsers – Expression evaluation is done by stacks by postfix or prefix using stacks in compilers.

### Activation Records – An activation record is data that keeps track of the procedure activities during the runtime of a program.

When the function is called, an activation record is created for it and keeps track of parameters and information like local variables, return address, static and dynamic links, and the return value.
This activation record is the fundamental part of programming languages and is implemented using a stack.
Web Browsers – Web Browsers use a stack to keep track of URLs that you have visited previously. When you visit a new page, it is added to the stack and when you hit the back button, the stack is popped and the previous URL is accessed.
To implement other Data Structures – Stacks are used to implement searches in Graphs and Trees, which are other complex data structures.


## Implementing Stacks
Stack Methods
There are various functions that are associated with a stack. They are,

### stack.isEmpty()  Time Complexity - O(1)
The stack.isEmpty() method returns True if the stack is empty. Else, returns False

### stack.length()  Time Complexity - O(1)
The stack.length() method returns the length of the stack.

### stack.top()  Time Complexity - O(1)
The stack.top() method returns a pointer/reference to the top element in the stack.

### stack.push(x)  Time Complexity - O(1)
The stack.push() method inserts the element, x to the top of the stack.

### stack.pop()  Time Complexity - O(1)
The stack.pop() method removes the top element of the stack and returns it.

## Stack Implementations
In Python, we can implement the stack by various methods. We are going to dive into two of the methods - the common method and the efficient method.

### Stack using a List
We use the list methods append and pop to implement a Stack.

```
class Stack:

    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = []

    def isEmpty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def length(self) -> int:
        return len(self.stack)

    def top(self) -> int:
        return self.stack[-1]  

    def push(self, x: int) -> None:
        self.x = x
        self.stack.append(x)       

    def pop(self) -> None:
        self.stack.pop()
```

### Stack using collection.Deque
Python collections are container classes that are used for data collection storage. They are highly optimized, are really fast, and have lots of methods built-in.

Deque is one such python collection that is used for inserting and removing items. We can use it to create a faster implementation of a stack.

```
from collections import deque
class Stack:

    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = deque()

    def isEmpty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def length(self) -> int:
        return len(self.stack)

    def top(self) -> int:
        return self.stack[-1]  

    def push(self, x: int) -> None:
        self.x = x
        self.stack.append(x)   

    def pop(self) -> None:
        self.stack.pop()
```

URL: https://www.section.io/engineering-education/stack-data-structure-python/