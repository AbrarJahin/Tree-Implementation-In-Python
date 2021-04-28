class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		 self.val = val
		 self.left = left
		 self.right = right

	def __repr__(self) -> str:
		return "TreeNode Class"

	def __str__(self) -> str:
		return str(self.val) + "[" + str(self.left) + ", " + str(self.right) + "]"

	def getHeight(self, node: TreeNode)-> int:
		if node is None: return 0
		else: return max(height(node.left), height(node.right)) + 1

	def printTreeInorder(self, node):
		if node.left is not None: printtree(node.left)
		print(node.val + ", ")
		if node.right is not None: printtree(node.right)