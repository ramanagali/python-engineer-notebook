# Queue implementation in Python FIFO
# linear data structure
# O(n) time complexity


class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.display()
    q.enqueue(5)

    q.display()

    q.dequeue()

    print("After removing an element")
    q.display()

    q.dequeue()
    q.display()
