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

    def preorder(self):

        print(self.key, end=' ')

        if self.lc:
            self.lc.preorder()
        if self.rc:
            self.rc.preorder()

    def inorder(self):

        if self.lc:
            self.lc.inorder()

        if self.key:
            print(self.key, end=' ')

        if self.rc:
            self.rc.inorder()

    def postorder(self):
        if self.lc:
            self.lc.postorder()

        if self.rc:
            self.rc.postorder()

        if self.key:
            print(self.key, end=' ')

    def delete(self, data):
        # if tree is not empty
        if self.key is None:
            print('Tree is empty')
            return

        # it no empty search
        if data < self.key:
            if self.lc:
                self.lc = self.lc.delete(data)
            else:
                print('Given node is not present in tree')
        elif data > self.key:
            if self.rc:
                self.rc = self.rc.delete(data)
            else:
                print('Given node is not present in tree')
        # delete
        else:
            # check left subt
            if self.lc is None:
                temp = self.rc
                self = None
                return temp
            if self.rc is None:
                temp = self.lc
                self = None
                return temp
            # delete if more more than 1 child nodes
            node = self.rc  # check smallest value at right side
            while node.lc:
                node = node.lc
            self.key = node.key
            self.rc = self.rc.delete(node.key)
            return self

    def min_node(self):
        curr = self
        while curr.lc:
            curr = curr.lc
        print('node with smallest key is :', curr.key)

    def max_node(self):
        curr = self
        while curr.rc:
            curr = curr.rc
        print('node with largest key is :', curr.key)


if __name__ == '__main__':
    root = BST(10)

    list1 = [6, 3, 1, 6, 4, 93, 3, 7, 83, 77, 24]
    for i in list1:
        root.insert(i)

    root.search(4)
    print('Pre-order')
    root.preorder()
    print()
    print('Inorder')
    root.inorder()
    print()
    print('Post Order')
    root.postorder()
    print()

    root.delete(6)
    print('After Delete-Pre-order')
    root.preorder()

    root.min_node()
    root.max_node()
