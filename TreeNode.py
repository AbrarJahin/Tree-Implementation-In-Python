class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		 self.val = val
		 self.left = left
		 self.right = right

	def __repr__(self) -> str:
		return "TreeNode Class"

	def __str__(self) -> str:
		return str(self.val) + "[" + str(self.left) + ", " + str(self.right) + "]"

	def getHeight(self)-> int:
		if self.left is None and self.right is None: return 1
		else: return max(self.left.getHeight(), self.right.getHeight()) + 1

	def printTreeInorder(self) -> None:
		if self.val is None: return
		if self.left is not None: self.left.printTreeInorder()
		print(self.val + ", ")
		if self.right is not None: self.right.printTreeInorder()