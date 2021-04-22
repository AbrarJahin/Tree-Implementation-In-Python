from TreeNode import TreeNode

class BST:
    # default constructor
    def __init__(self):
        self.root = None    #TreeNode()

    # a method for printing data members
    def __repr__(self) -> str:
        return "TreeNode"

    def __str__(self) -> str:
        return root

    def isKeyExist(self, key: str) -> bool:
        return self.search(key) is not None

    def search(self, key: str, root = "default") -> bool:
        if root == "default": root = self.root
        if not root: return None
        elif root.val == key: return root
        elif root.val>key: return self.search(key, root.left)
        elif root.val<key: return self.search(key, root.right)

    def insert(self, key: str, root = "default") -> str:
        if root == "default":
            if self.root == None:
                self.root = TreeNode()
                self.root.val = key
                return self.root
            else: root = self.root
        if not root:
            root = TreeNode()
            root.val = key
        elif key < root.val:
            root.left = self.insert(key, root.left)
        elif key > root.val:
            root.right = self.insert(key, root.right)
        else:
            print("error insert")
        return root

    def findMinNode(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root

    def delete(self, key: str, root = "default") -> None:
        if root == "default": root = self.root
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