from TreeNode import TreeNode

class SplayNode(TreeNode):
	def  __init__(self, data, left = None, right = None):
		TreeNode.__init__(self, data, left, right)
		self.parent = None

	def __repr__(self) -> str:
		return "SplayNode Class"

	def __str__(self) -> str:
		return str(self.val) + "[" + str(self.left) + ", " + str(self.right) + "]"