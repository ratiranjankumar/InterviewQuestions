class CircularQueue:
    def __init__(self, max_length):
        self.queue = {}
        self.max_length = max_length
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.max_length:
            # Remove the latest added element
            last_index = (self.tail - 1) % self.max_length
            del self.queue[last_index]
            self.tail = last_index
            self.size -= 1
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_length
        self.size += 1
        print(self.size)

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
            return None
        value = self.queue[self.tail]
        del self.queue[self.tail]
        self.tail = (self.tail + 1) % self.max_length
        self.size -= 1
        return value

    def display(self):
        if self.size == 0:
            print("Queue is empty")
            return
        index = self.tail
        for _ in range(self.size):
            print(self.queue[index], end=" ")
            index = (index + 1) % self.max_length
        print()

# Example 
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()  # Output: 1 2 3 4 5
cq.enqueue(6)
cq.display()  # Output: 2 3 4 5 6
cq.dequeue()
cq.display()  # Output: 3 4 5 6
