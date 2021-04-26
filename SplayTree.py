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

	def searchTreeHelper(self, node, key):
		if node == None or key == node.val:
			return node

		if key < node.val:
			return self.searchTreeHelper(node.left, key)
		return self.searchTreeHelper(node.right, key)

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

	def joinTrees(self, firstTree, secondTree):
		if firstTree == None: return secondTree
		if secondTree == None: return firstTree
		x = self.maximum(firstTree)
		self.splayOperation(x)
		x.right = secondTree
		secondTree.parent = x
		return x

	def search(self, key):
		x = self.searchTreeHelper(self.root, key)
		if x != None:
			self.splayOperation(x)

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
		node =  SplayNode(key)
		y = None
		x = self.root

		while x != None:
			y = x
			if node.val < x.val:
				x = x.left
			else:
				x = x.right

		# y is parent of x
		node.parent = y
		if y == None:
			self.root = node
		elif node.val < y.val:
			y.left = node
		else:
			y.right = node
		# splay the node
		self.splayOperation(node)

	def delete(self, data):
		self.deleteNodeHelper(self.root, data)
	def deleteNodeHelper(self, node, key):
		x = None
		t = None 
		s = None
		while node != None:
			if node.val == key:
				x = node

			if node.val <= key:
				node = node.right
			else:
				node = node.left

		if x == None:
			print("Couldn't find key in the tree")
			return
		
		# split operation
		self.splayOperation(x)
		if x.right != None:
			t = x.right
			t.parent = None
		else:
			t = None

		s = x
		s.right = None
		x = None

		# join operation
		if s.left != None:
			s.left.parent = None

		self.root = self.joinTrees(s.left, t)
		s = None
