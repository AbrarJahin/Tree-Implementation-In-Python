from TreeNode import TreeNode

class BST:
    # default constructor
    def __init__(self, maxNoOfElement = 100):
        self.root = None    #TreeNode()

    # a method for printing data members
    def __repr__(self) -> str:
        return "TreeNode"

    def __str__(self) -> str:
        return root

    def search(self, key: str, root = self.root) -> bool:
        if not root: return False
        elif root.val == key: return True
        elif root.val>key: root.left = self.search(key, root.left)
        elif root.val<key: root.right = self.search(key, root.right)

    def insert(self, key: str, root = self.root) -> str:
        if not root:
            root = TreeNode(key)
        elif key < root.val:
            root.left = self.insert(key, root.left)
        elif key > root.val:
            root.right = self.insert(key, root.right)
        else:
            print("error insert")

    def findMinNode(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root

    def delete(self, key: str, root = self.root) -> None:
        if not root: return None
        elif root.val>key: root.left = self.delete(key, root.left)
        elif root.val<key: root.right = self.delete(key, root.right)
        elif root.val == key:
            #delete operation here
            if not root.left: return root.right
            if not root.right: return root.left
            swapNode = self.findMinNode(root.right)
            root.val = swapNode.val
            root.right = self.delete(swapNode.val, root.right)