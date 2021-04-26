import sys
from SplayNode import SplayNode

class SplayTree:
	def __init__(self):
		self.root = None

	# a method for printing data members
	def __repr__(self) -> str:
		return "SplayTree"

	def __str__(self) -> str:
		return str(self.root.val) + "[" + str(self.root.left) + ", " + str(self.root.right) + "]"

	# Move node to the root of the tree
	def splayOperation(self, node):
		while node.parent != None:
			if node.parent.parent == None:
				if node == node.parent.left:
					# zig rotation
					self.rightRotate(node.parent)
				else:
					# zag rotation
					self.leftRotate(node.parent)
			elif node == node.parent.left and node.parent == node.parent.parent.left:
				# zig-zig rotation
				self.rightRotate(node.parent.parent)
				self.rightRotate(node.parent)
			elif node == node.parent.right and node.parent == node.parent.parent.right:
				# zag-zag rotation
				self.leftRotate(node.parent.parent)
				self.leftRotate(node.parent)
			elif node == node.parent.right and node.parent == node.parent.parent.left:
				# zig-zag rotation
				self.leftRotate(node.parent)
				self.rightRotate(node.parent)
			else:
				# zag-zig rotation
				self.rightRotate(node.parent)
				self.leftRotate(node.parent)

	def search(self, key):
		x = self.searchTreeHelper(self.root, key)
		if x != None: self.splayOperation(x)
	def searchTreeHelper(self, node, key):
		if node == None or key == node.val: return node
		elif key < node.val: return self.searchTreeHelper(node.left, key)
		else: return self.searchTreeHelper(node.right, key)

	# rotate left at node x
	def leftRotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != None: y.left.parent = x
		y.parent = x.parent
		if x.parent == None: self.root = y
		elif x == x.parent.left: x.parent.left = y
		else: x.parent.right = y
		y.left = x
		x.parent = y

	# rotate right at node x
	def rightRotate(self, x):
		y = x.left
		x.left = y.right
		if y.right != None:
			y.right.parent = x
		y.parent = x.parent;
		if x.parent == None: self.root = y
		elif x == x.parent.right: x.parent.right = y
		else: x.parent.left = y
		y.right = x
		x.parent = y

	def joinTrees(self, firstTree, secondTree):
		if firstTree == None: return secondTree
		if secondTree == None: return firstTree
		x = self.maximum(firstTree)
		self.splayOperation(x)
		x.right = secondTree
		secondTree.parent = x
		return x

	def isKeyExist(self, key: str) -> bool:
		return self.search(key) is not None

	def minimum(self, node):
		while node.left != None:
			node = node.left
		return node

	def maximum(self, node):
		while node.right != None:
			node = node.right
		return node

	def insert(self, key):
		x, y, nodeToInsert = self.root, None, SplayNode(key)
		while x != None:
			y = x
			if nodeToInsert.val < x.val: x = x.left
			else: x = x.right
		# y is parent of x
		nodeToInsert.parent = y
		if y == None: self.root = nodeToInsert
		elif nodeToInsert.val < y.val: y.left = nodeToInsert
		else: y.right = nodeToInsert
		# Extra Operation - Splay
		self.splayOperation(nodeToInsert)

	def delete(self, data):
		self.deleteNodeHelper(self.root, data)
	def deleteNodeHelper(self, node, key):
		x, t, s = None, None, None
		while node != None:
			if node.val == key: x = node
			if node.val <= key: node = node.right
			else: node = node.left
		if x == None: return # Key not found
		# split operation
		self.splayOperation(x)
		if x.right != None: t, t.parent = x.right, None
		else: t = None
		s, s.right, x = x, None, None
		# join operation
		if s.left != None: s.left.parent = None
		self.root, s = self.joinTrees(s.left, t), None