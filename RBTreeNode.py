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

    def __repr__(self) -> str:
        return "RBTreeNode Class"

    def __str__(self) -> str:
        return str(self.val) + "[" + str(self.left) + ", " + str(self.right) + "]"
