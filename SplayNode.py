from TreeNode import TreeNode

class SplayNode(TreeNode):
	def  __init__(self, data, left = None, right = None):
		TreeNode.__init__(self, data, left, right)
		self.parent = None