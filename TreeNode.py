class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		 self.val = val
		 self.left = left
		 self.right = right

	def __repr__(self) -> str:
		return "TreeNode Class"

	def __str__(self) -> str:
		return str(self.val) + "[" + str(self.left) + ", " + str(self.right) + "]"
