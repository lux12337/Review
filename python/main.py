from data_structures import linked_list as list
from data_structures import bst as bst
from collections import deque

# q = deque()
# q.append('test')
# q.append('hello')
# print(q)
# print(q.pop())

bst = bst.BST()
bst.insert(25)
bst.insert(15)
bst.insert(10)
bst.insert(4)
bst.insert(12)
bst.insert(22)
bst.insert(18)
bst.insert(24)
bst.insert(50)
bst.insert(35)
bst.insert(31)
bst.insert(44)
bst.insert(70)
bst.insert(66)
bst.insert(90)

bst.inorder()
bst.preorder()
bst.postorder()
