from TreeNode import TreeNode

class RBTreeNode(TreeNode):
    color = ""

    def __init__(self, nodeParent="black", nodeColor="black", val=0, left=None, right=None):  
        TreeNode.__init__(self, val, left, right)
        self.color = nodeColor
        self.parent = nodeParent