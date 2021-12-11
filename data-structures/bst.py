class BST:
    def __init__(self, key):
        self.key = key
        self.lc = None
        self.rc = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        # if data is same as root, return
        if self.key == data:
            return

        # if data is less than root, insert in left subtree
        if self.key > data:
            if self.lc:
                self.lc.insert(data)
            else:
                self.lc = BST(data)
        else:  # data is greater than root, insert in right subtree
            if self.rc:
                self.rc.insert(data)
            else:
                self.rc = BST(data)

    def search(self, data):
        if self.key == data:
            print('Node Found')
            return
        if data < self.key:
            if self.lc:
                self.lc.search(data)
            else:
                print('Node is not present in tree')
        else:
            if self.rc:
                self.rc.search(data)
            else:
                print('Node is not present in tree')


if __name__ == '__main__':
    root = BST(10)

    list1 = [6, 3, 1, 6, 4, 93, 3, 7]
    for i in list1:
        root.insert(i)

    root.search(4)
