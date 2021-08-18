

# Stack
===================

A data structure that stores data in a First In, First Out (FIFO) manner. Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both of its ends. In this article, we’ll be looking at how to implement and use the queue data structure in Python.

For more background on the different data structures in Python, check out my articles on the List and Stack data structures.

Table of Contents
* Queue: Introduction
* Uses of Queues
* Implementing Queues

## Conclusion
Queue - An introduction
A Queue is a linear data structure in which data is stored in a First In, First Out manner. In a queue, the item that was added the earliest is removed first. The item that was added more recently is removed last. A queue can be compared to a real-life queue.

enqueue is a queue operation where you add an item at the back of a queue.

dequeue is a queue operation where you remove an item from the front of a queue.

## Uses of Queues
### Operating Systems - often maintain queues while implementing various low-level operations such as CPU Scheduling, Disk Scheduling, etc.
### Hardware - hardware interrupts are handled using queues.
### Internet - Website traffic handling.
And all other scenarios where a First In, First Out priority has to be implemented.

## Implementing Queues

Queue Methods

### queue.Enqueue()  Time Complexity -> O(1)
The queue.Enqueue() method adds an element at the rear of the queue.

### queue.Dequeue()  Time Complexity -> O(1)
The queue.Dequeue() method removes an element from the front of the queue.

### queue.Front()   Time Complexity -> O(1)
The queue.Front() method returns the front item from the queue.

### queue.Rear()   Time Complexity -> O(1)
The queue.Rear() method returns the rear item from the queue.

### queue.isEmpty()   Time Complexity -> O(1)
The queue.isEmpty() method returns True if the queue is empty, else returns False.

Queues can be implemented in various ways. Let us look at how to implement a queue using a list and using the collections.deque module in Python.

## Queue using a List
We can use the list methods insert and pop to implement a queue.

```
class Queue:

    def __init__(self):
        """
        Initializing Queue.
        """
        self.queue = []

    def isEmpty(self) -> bool:
        return True if len(self.queue) == 0 else False

    def front(self) -> int:
        return self.queue[-1]

    def rear(self) -> int:
        return self.queue[0]

    def enqueue(self, x: int) -> None:
        self.x = x
        self.queue.insert(0, x)       

    def dequeue(self) -> None:
        self.queue.pop()

 ```

## Queue using collections.Deque
The deque class from the python collections module can also be used to implement a queue. This method of implementing a queue is far more efficient because deque provides faster enqueue and dequeue operations.

```
from collections import deque
class Queue:

    def __init__(self):
        """
        Initializing Queue.
        """
        self.queue = deque()

    def isEmpty(self) -> bool:
        return True if len(self.queue) == 0 else False

    def front(self) -> int:
        return self.queue[-1]

    def rear(self) -> int:
        return self.queue[0]

    def enqueue(self, x: int) -> None:
        self.x = x
        self.queue.append(x)       

    def dequeue(self) -> None:
        self.queue.popleft()
```

URL: https://www.section.io/engineering-education/queue-data-structure-python/