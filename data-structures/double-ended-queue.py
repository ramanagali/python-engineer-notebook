# Deque implementaion in python
# O(1) is time complexity for all operations

# Function for double ended queue


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    d = Deque()
    print('isEmpty? ', d.isEmpty())
    d.addRear(8)
    d.addRear(5)
    d.addFront(7)
    d.addFront(10)
    print('size ', d.size())
    print('isEmpty? ', d.isEmpty())
    d.addRear(11)
    print('removeRear ', d.removeRear())
    print('removeFront ', d.removeFront())
    d.addFront(55)
    d.addRear(45)
    print('items ', d.items)
