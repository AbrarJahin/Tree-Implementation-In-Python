import sys

class RBTreeNode():
	def __init__(self, item):
		self.val = item
		self.left = None
		self.right = None

		self.color = 1
		self.parent = None

class RedBlackTree():
	def __init__(self):
		self.TRootNull = RBTreeNode(0)
		self.TRootNull.color = 0
		self.TRootNull.left = None
		self.TRootNull.right = None
		self.root = self.TRootNull

	# Search the tree
	def search(self, k):
		return self.searchTreeHelper(self.root, k)
	def searchTreeHelper(self, node, key):
		if node == TNULL or key == node.val: return node
		elif key < node.val: return self.searchTreeHelper(node.left, key)
		else: return self.searchTreeHelper(node.right, key)

	# Node deletion
	def delete(self, item):
		self.deleteNodeHelper(self.root, item)
	def deleteNodeHelper(self, node, key):
		z = self.TRootNull
		while node != self.TRootNull:
			if node.val == key: z = node
			if node.val <= key: node = node.right
			else: node = node.left
		if z == self.TRootNull:
			print("Cannot find key in the tree")
			return
		y = z
		y_original_color = y.color
		if z.left == self.TRootNull:
			x = z.right
			self.rbTransplant(z, z.right)
		elif (z.right == self.TRootNull):
			x = z.left
			self.rbTransplant(z, z.left)
		else:
			y = self.minimum(z.right)
			y_original_color = y.color
			x = y.right
			if y.parent == z: x.parent = y
			else:
				self.rbTransplant(y, y.right)
				y.right = z.right
				y.right.parent = y
			self.rbTransplant(z, y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if y_original_color == 0: self.deleteFixupSubroutine(x)

	# Balancing the tree after deletion
	def deleteFixupSubroutine(self, x):
		while x != self.root and x.color == 0:
			if x == x.parent.left:
				s = x.parent.right
				if s.color == 1:
					s.color = 0
					x.parent.color = 1
					self.leftRotate(x.parent)
					s = x.parent.right

				if s.left.color == 0 and s.right.color == 0:
					s.color = 1
					x = x.parent
				else:
					if s.right.color == 0:
						s.left.color = 0
						s.color = 1
						self.rightRotate(s)
						s = x.parent.right

					s.color = x.parent.color
					x.parent.color = 0
					s.right.color = 0
					self.leftRotate(x.parent)
					x = self.root
			else:
				s = x.parent.left
				if s.color == 1:
					s.color = 0
					x.parent.color = 1
					self.rightRotate(x.parent)
					s = x.parent.left

				if s.right.color == 0 and s.right.color == 0:
					s.color = 1
					x = x.parent
				else:
					if s.left.color == 0:
						s.right.color = 0
						s.color = 1
						self.leftRotate(s)
						s = x.parent.left

					s.color = x.parent.color
					x.parent.color = 0
					s.left.color = 0
					self.rightRotate(x.parent)
					x = self.root
		x.color = 0

	def rbTransplant(self, u, v):
		if u.parent == None: self.root = v
		elif u == u.parent.left: u.parent.left = v
		else: u.parent.right = v
		v.parent = u.parent

	# Node insert
	def insert(self, key):
		node = RBTreeNode(key)
		node.parent = None
		node.val = key
		node.left = self.TRootNull
		node.right = self.TRootNull
		node.color = 1
		y = None
		x = self.root
		while x != self.TRootNull:
			y = x
			if node.val < x.val: x = x.left
			else: x = x.right
		node.parent = y
		if y == None: self.root = node
		elif node.val < y.val: y.left = node
		else: y.right = node
		if node.parent == None:
			node.color = 0
			return
		if node.parent.parent == None: return
		self.insertFixupSubroutine(node)

	# Balance the tree after insertion
	def insertFixupSubroutine(self, k):
		while k.parent.color == 1:
			if k.parent == k.parent.parent.right:
				u = k.parent.parent.left
				if u.color == 1:
					u.color = 0
					k.parent.color = 0
					k.parent.parent.color = 1
					k = k.parent.parent
				else:
					if k == k.parent.left:
						k = k.parent
						self.rightRotate(k)
					k.parent.color = 0
					k.parent.parent.color = 1
					self.leftRotate(k.parent.parent)
			else:
				u = k.parent.parent.right

				if u.color == 1:
					u.color = 0
					k.parent.color = 0
					k.parent.parent.color = 1
					k = k.parent.parent
				else:
					if k == k.parent.right:
						k = k.parent
						self.leftRotate(k)
					k.parent.color = 0
					k.parent.parent.color = 1
					self.rightRotate(k.parent.parent)
			if k == self.root:
				break
		self.root.color = 0

	def minimum(self, node):
		while node.left != self.TRootNull:
			node = node.left
		return node

	def maximum(self, node):
		while node.right != self.TRootNull:
			node = node.right
		return node

	def successor(self, x):
		if x.right != self.TRootNull: return self.minimum(x.right)
		y = x.parent
		while y != self.TRootNull and x == y.right:
			x = y
			y = y.parent
		return y

	def predecessor(self,  x):
		if (x.left != self.TRootNull): return self.maximum(x.left)
		y = x.parent
		while y != self.TRootNull and x == y.left:
			x = y
			y = y.parent
		return y

	def leftRotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != self.TRootNull: y.left.parent = x
		y.parent = x.parent
		if x.parent == None: self.root = y
		elif x == x.parent.left: x.parent.left = y
		else: x.parent.right = y
		y.left = x
		x.parent = y

	def rightRotate(self, x):
		y = x.left
		x.left = y.right
		if y.right != self.TRootNull: y.right.parent = x
		y.parent = x.parent
		if x.parent == None: self.root = y
		elif x == x.parent.right: x.parent.right = y
		else: x.parent.left = y
		y.right = x
		x.parent = y

####################################################################
	# Preorder
	def preorder(self):
		self.preOrderHelper(self.root)
	def preOrderHelper(self, node):
		if node != TNULL:
			sys.stdout.write(node.val + " ")
			self.preOrderHelper(node.left)
			self.preOrderHelper(node.right)

	# Inorder
	def inorder(self):
		self.inOrderHelper(self.root)
	def inOrderHelper(self, node):
		if node != TNULL:
			self.inOrderHelper(node.left)
			sys.stdout.write(node.val + " ")
			self.inOrderHelper(node.right)

	# Postorder
	def postorder(self):
		self.postOrderHelper(self.root)
	def postOrderHelper(self, node):
		if node != TNULL:
			self.postOrderHelper(node.left)
			self.postOrderHelper(node.right)
			sys.stdout.write(node.val + " ")

	# Printing the tree
	def printTree(self):
		self.printHelper(self.root, "", True)
	def printHelper(self, node, indent, last):
		if node != self.TRootNull:
			sys.stdout.write(indent)
			if last:
				sys.stdout.write("R----")
				indent += "     "
			else:
				sys.stdout.write("L----")
				indent += "|    "

			s_color = "RED" if node.color == 1 else "BLACK"
			print(str(node.val) + "(" + s_color + ")")
			self.printHelper(node.left, indent, False)
			self.printHelper(node.right, indent, True)
####################################################################

if __name__ == "__main__":
	bst = RedBlackTree()
	bst.insert(55)
	bst.insert(40)
	bst.insert(65)
	bst.insert(60)
	bst.insert(75)
	bst.insert(57)

	bst.printTree()

	print("\nAfter deleting an element")
	bst.delete(40)
	bst.printTree()