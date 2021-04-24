from TreeNode import TreeNode
from enum import Enum

class Color(Enum):
    RED = 1
    BLACK = 0

class RBTreeNode(TreeNode):
    def __init__(self, val=0, nodeParent=None, nodeColor="black", left=None, right=None):  
        TreeNode.__init__(self, val, left, right)
        self.color = Color.BLACK
        self.parent = nodeParent