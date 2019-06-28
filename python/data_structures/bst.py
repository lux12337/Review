class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def preorder(self):
        if self:
            print(str(self.data) + ' ', end='')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()


    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data) + ' ', end='')
            if self.right:
                self.right.inorder()


    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.data) + ' ', end='')


class BST(object):
    def __init__(self):
        self.root = None


    def insertNode(self, currentNode, data):
        if currentNode.data == data:
            print('Value already in tree.')
            return
        if currentNode.data < data:
            if currentNode.right:
                self.insertNode(currentNode.right, data)
            else:
                currentNode.right = TreeNode(data)
        else:
            if currentNode.left:
                self.insertNode(currentNode.left, data)
            else:
                currentNode.left = TreeNode(data)


    def insert(self, data):
        if self.root:
            self.insertNode(self.root, data)
        else:
            self.root = TreeNode(data)


    def inorder(self):
        if self.root:
            self.root.inorder()
            print('')
        else:
            print('No tree present')


    def preorder(self):
        if self.root:
            self.root.preorder()
            print('')
        else:
            print('No tree present')


    def postorder(self):
        if self.root:
            self.root.postorder()
            print('')
        else:
            print('No tree present')
