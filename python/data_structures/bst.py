class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Prints values in preorder order starting from node
    def preorder(self):
        if self:
            print(str(self.data) + ' ', end='')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

# Prints values in inorder order starting from node
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data) + ' ', end='')
            if self.right:
                self.right.inorder()

# Prints values in postorder order starting from node
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.data) + ' ', end='')

# Prints values in preorder order starting from node
    def preorderIter(self):
        stack = []
        current = self
        while True:
            if current:
                print(str(current.data) + ' ', end='')
                stack.append(current)
                current = current.left
            elif stack != []:
                current = stack.pop()
                current = current.right
            else:
                break

# Prints values in inorder order starting from node
    def inorderIter(self):
        stack = []
        current = self
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack != []:
                current = stack.pop()
                print(str(current.data) + ' ', end='')
                current = current.right
            else:
                break

# Pritns values in postorder order starting from node

class BST(object):
    def __init__(self):
        self.root = None

# Helper function for inserting a node in BST
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

# Inserts node in BST tree
    def insert(self, data):
        if self.root:
            self.insertNode(self.root, data)
        else:
            self.root = TreeNode(data)

# Delete node in BST tree

# Calls preorder function on root of BST
    def preorder(self):
        if self.root:
            self.root.preorder()
            print('')
        else:
            print('No tree present')

# Calls inorder function on root of BST
    def inorder(self):
        if self.root:
            self.root.inorder()
            print('')
        else:
            print('No tree present')

# Calls postorder function on root of BST
    def postorder(self):
        if self.root:
            self.root.postorder()
            print('')
        else:
            print('No tree present')

# Calls iterative inorder function on root of BST
    def inorderIter(self):
        if self.root:
            self.root.inorderIter()
            print('')
        else:
            print('No tree present')

# Calls iterative preorder function on root of BST
    def preorderIter(self):
        if self.root:
            self.root.preorderIter()
            print('')
        else:
            print('No tree present')
