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

queue = Queue()
queue.enqueue(9)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(50)
print(queue.queue)
print(queue.front())
print(queue.rear())
queue.dequeue()
print(queue.queue)
