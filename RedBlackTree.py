import sys
from RBTreeNode import RBTreeNode, Color

class RedBlackTree():
	def __init__(self):
		self.TRootNull = RBTreeNode("Default Value that can't be given")
		self.TRootNull.color = Color.BLACK
		self.TRootNull.left = None
		self.TRootNull.right = None
		self.root = self.TRootNull

	# Search the tree
	def search(self, key: str) -> RBTreeNode:
		return self.searchTreeHelper(self.root, key)
	def searchTreeHelper(self, node: RBTreeNode, key: str) -> RBTreeNode:
		if node == self.TRootNull or key == node.val:
			return node if node.val==key else None
		elif key < node.val:
			return self.searchTreeHelper(node.left, key)
		else:
			return self.searchTreeHelper(node.right, key)

	def isKeyExist(self, key: str) -> bool:
		return self.search(key) is not None

	# Node deletion
	def delete(self, item: str) -> None:
		self.deleteNodeHelper(self.root, item)
	def deleteNodeHelper(self, node: RBTreeNode, key: str) -> None:
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
			y = self.findMinimum(z.right)
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
		if y_original_color == Color.BLACK: self.deleteFixupSubroutine(x)

	# Balancing the tree after deletion
	def deleteFixupSubroutine(self, x: RBTreeNode) -> None:
		while x != self.root and x.color == Color.BLACK:
			if x == x.parent.left:
				s = x.parent.right
				if s.color == Color.RED:
					s.color = Color.BLACK
					x.parent.color = Color.RED
					self.leftRotate(x.parent)
					s = x.parent.right
				if s.left.color == Color.BLACK and s.right.color == Color.BLACK:
					s.color = Color.RED
					x = x.parent
				else:
					if s.right.color == Color.BLACK:
						s.left.color = Color.BLACK
						s.color = Color.RED
						self.rightRotate(s)
						s = x.parent.right
					s.color = x.parent.color
					x.parent.color = Color.BLACK
					s.right.color = Color.BLACK
					self.leftRotate(x.parent)
					x = self.root
			else:
				s = x.parent.left
				if s.color == Color.RED:
					s.color = Color.BLACK
					x.parent.color = Color.RED
					self.rightRotate(x.parent)
					s = x.parent.left
				if s.right.color == Color.BLACK and s.right.color == Color.BLACK:
					s.color = Color.RED
					x = x.parent
				else:
					if s.left.color == Color.BLACK:
						s.right.color = Color.BLACK
						s.color = Color.RED
						self.leftRotate(s)
						s = x.parent.left
					s.color = x.parent.color
					x.parent.color = Color.BLACK
					s.left.color = Color.BLACK
					self.rightRotate(x.parent)
					x = self.root
		x.color = Color.BLACK

	def rbTransplant(self, u: RBTreeNode, v: RBTreeNode) -> None:
		if u.parent == None: self.root = v
		elif u == u.parent.left: u.parent.left = v
		else: u.parent.right = v
		v.parent = u.parent

	# Node insert
	def insert(self, key: str) -> None:
		node = RBTreeNode(key)
		node.left = self.TRootNull
		node.right = self.TRootNull
		node.color = Color.RED
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
			node.color = Color.BLACK
			return
		if node.parent.parent == None: return
		self.insertFixupSubroutine(node)

	# Balance the tree after insertion
	def insertFixupSubroutine(self, k: str) -> None:
		while k.parent.color == Color.RED:
			if k.parent == k.parent.parent.right:
				u = k.parent.parent.left
				if u.color == Color.RED:
					u.color = Color.BLACK
					k.parent.color = Color.BLACK
					k.parent.parent.color = Color.RED
					k = k.parent.parent
				else:
					if k == k.parent.left:
						k = k.parent
						self.rightRotate(k)
					k.parent.color = Color.BLACK
					k.parent.parent.color = Color.RED
					self.leftRotate(k.parent.parent)
			else:
				u = k.parent.parent.right

				if u.color == Color.RED:
					u.color = Color.BLACK
					k.parent.color = Color.BLACK
					k.parent.parent.color = Color.RED
					k = k.parent.parent
				else:
					if k == k.parent.right:
						k = k.parent
						self.leftRotate(k)
					k.parent.color = Color.BLACK
					k.parent.parent.color = Color.RED
					self.rightRotate(k.parent.parent)
			if k == self.root:
				break
		self.root.color = Color.BLACK

	def findMinimum(self, node: RBTreeNode) -> RBTreeNode:
		while node.left != self.TRootNull:
			node = node.left
		return node

	def findMaximum(self, node: RBTreeNode) -> RBTreeNode:
		while node.right != self.TRootNull:
			node = node.right
		return node

	def leftRotate(self, x: RBTreeNode) -> None:
		y = x.right
		x.right = y.left
		if y.left != self.TRootNull: y.left.parent = x
		y.parent = x.parent
		if x.parent == None: self.root = y
		elif x == x.parent.left: x.parent.left = y
		else: x.parent.right = y
		y.left = x
		x.parent = y

	def rightRotate(self, x: RBTreeNode) -> None:
		y = x.left
		x.left = y.right
		if y.right != self.TRootNull: y.right.parent = x
		y.parent = x.parent
		if x.parent == None: self.root = y
		elif x == x.parent.right: x.parent.right = y
		else: x.parent.left = y
		y.right = x
		x.parent = y
