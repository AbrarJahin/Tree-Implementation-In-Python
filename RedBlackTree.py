import sys
from RBTreeNode import RBTreeNode, Color

class RedBlackTree():
	def __init__(self):
		self.TRootNull = RBTreeNode(None)
		self.TRootNull.color = Color.BLACK
		self.TRootNull.left = None
		self.TRootNull.right = None
		self.root = self.TRootNull

	# a method for printing data members
	def __repr__(self) -> str:
		return "RedBlackTree"

	def __str__(self) -> str:
		return str(self.root.val) + " : " + str(self.root.color)\
				+ "[" + str(self.root.left) + " : " + str(self.root.left.color)\
			    + ", " + str(self.root.right) + " : " + str(self.root.right.color) + "]"

	# Search the tree
	def search(self, key: str) -> RBTreeNode:
		return self.searchTreeHelper(self.root, key)
	def searchTreeHelper(self, node: RBTreeNode, key: str) -> RBTreeNode:
		if node == self.TRootNull or key == node.val: return node if node.val==key else None
		elif key < node.val: return self.searchTreeHelper(node.left, key)
		else: return self.searchTreeHelper(node.right, key)

	def isKeyExist(self, key: str) -> bool:
		return self.search(key) is not None

	# Node deletion
	def delete(self, key: str) -> None:
		self.deleteNodeHelper(self.root, key)
	def deleteNodeHelper(self, node: RBTreeNode, key: str) -> None:
		zNode = self.TRootNull
		while node != self.TRootNull:
			if node.val == key: zNode = node
			if node.val <= key: node = node.right
			else: node = node.left
		if zNode == self.TRootNull: return #Key Not Found
		yNode = zNode
		colorYPrev = yNode.color
		if zNode.left == self.TRootNull:
			xNode = zNode.right
			self.rbTransplant(zNode, zNode.right)
		elif (zNode.right == self.TRootNull):
			xNode = zNode.left
			self.rbTransplant(zNode, zNode.left)
		else:
			yNode = self.findMinimum(zNode.right)
			colorYPrev, xNode = yNode.color, yNode.right
			if yNode.parent == zNode: xNode.parent = yNode
			else:
				self.rbTransplant(yNode, yNode.right)
				yNode.right = zNode.right
				yNode.right.parent = yNode
			self.rbTransplant(zNode, yNode)
			yNode.left = zNode.left
			yNode.left.parent, yNode.color = yNode, zNode.color
		if colorYPrev == Color.BLACK: self.deleteFixupSubroutine(xNode)

	# Balancing the tree after deletion
	def deleteFixupSubroutine(self, xNode: RBTreeNode) -> None:
		while xNode != self.root and xNode.color == Color.BLACK:
			if xNode == xNode.parent.left:
				sNode = xNode.parent.right
				if sNode.color == Color.RED:
					sNode.color, xNode.parent.color = Color.BLACK, Color.RED
					self.leftRotate(xNode.parent)
					sNode = xNode.parent.right
				if sNode.left.color == Color.BLACK and sNode.right.color == Color.BLACK:
					sNode.color, xNode = Color.RED, xNode.parent
				else:
					if sNode.right.color == Color.BLACK:
						sNode.left.color = Color.BLACK
						sNode.color = Color.RED
						self.rightRotate(sNode)
						sNode = xNode.parent.right
					sNode.color, sNode.right.color, xNode.parent.color = xNode.parent.color, Color.BLACK, Color.BLACK
					self.leftRotate(xNode.parent)
					xNode = self.root
			else:
				sNode = xNode.parent.left
				if sNode.color == Color.RED:
					sNode.color, xNode.parent.color = Color.BLACK, Color.RED
					self.rightRotate(xNode.parent)
					sNode = xNode.parent.left
				if sNode.right.color == Color.BLACK and sNode.right.color == Color.BLACK:
					sNode.color = Color.RED
					xNode = xNode.parent
				else:
					if sNode.left.color == Color.BLACK:
						sNode.right.color, sNode.color = Color.BLACK, Color.RED
						self.leftRotate(sNode)
						sNode = xNode.parent.left
					sNode.color = xNode.parent.color
					xNode.parent.color, sNode.left.color = Color.BLACK, Color.BLACK
					self.rightRotate(xNode.parent)
					xNode = self.root
		xNode.color = Color.BLACK

	def rbTransplant(self, firstNode: RBTreeNode, secondNode: RBTreeNode) -> None:
		if firstNode.parent == None: self.root = secondNode
		elif firstNode == firstNode.parent.left: firstNode.parent.left = secondNode
		else: firstNode.parent.right = secondNode
		secondNode.parent = firstNode.parent

	# Node insert
	def insert(self, key: str) -> None:
		node = RBTreeNode(key)
		node.left = self.TRootNull
		node.right = self.TRootNull
		node.color = Color.RED
		yNode = None
		xNode = self.root
		while xNode != self.TRootNull:
			yNode = xNode
			if node.val < xNode.val: xNode = xNode.left
			else: xNode = xNode.right
		node.parent = yNode
		if yNode == None: self.root = node
		elif node.val < yNode.val: yNode.left = node
		else: yNode.right = node
		if node.parent == None:
			node.color = Color.BLACK
			return
		if node.parent.parent == None: return
		self.insertFixupSubroutine(node)

	# Balance the tree after insertion
	def insertFixupSubroutine(self, node: RBTreeNode) -> None:
		while node.parent.color == Color.RED:
			if node.parent == node.parent.parent.right:
				sibling = node.parent.parent.left
				if sibling.color == Color.RED:
					sibling.color = Color.BLACK
					node.parent.color = Color.BLACK
					node.parent.parent.color = Color.RED
					node = node.parent.parent
				else:
					if node == node.parent.left:
						node = node.parent
						self.rightRotate(node)
					node.parent.color = Color.BLACK
					node.parent.parent.color = Color.RED
					self.leftRotate(node.parent.parent)
			else:
				sibling = node.parent.parent.right
				if sibling.color == Color.RED:
					sibling.color = Color.BLACK
					node.parent.color = Color.BLACK
					node.parent.parent.color = Color.RED
					node = node.parent.parent
				else:
					if node == node.parent.right:
						node = node.parent
						self.leftRotate(node)
					node.parent.color = Color.BLACK
					node.parent.parent.color = Color.RED
					self.rightRotate(node.parent.parent)
			if node == self.root:
				break
		self.root.color = Color.BLACK

	def findMinimum(self, node: RBTreeNode) -> RBTreeNode:
		while node.left != self.TRootNull: node = node.left
		return node

	def findMaximum(self, node: RBTreeNode) -> RBTreeNode:
		while node.right != self.TRootNull: node = node.right
		return node

	def leftRotate(self, xNode: RBTreeNode) -> None:
		yNode = xNode.right
		xNode.right = yNode.left
		if yNode.left != self.TRootNull: yNode.left.parent = xNode
		yNode.parent = xNode.parent
		if xNode.parent == None: self.root = yNode
		elif xNode == xNode.parent.left: xNode.parent.left = yNode
		else: xNode.parent.right = yNode
		yNode.left = xNode
		xNode.parent = yNode

	def rightRotate(self, xNode: RBTreeNode) -> None:
		yNode = xNode.left
		xNode.left = yNode.right
		if yNode.right != self.TRootNull: yNode.right.parent = xNode
		yNode.parent = xNode.parent
		if xNode.parent == None: self.root = yNode
		elif xNode == xNode.parent.right: xNode.parent.right = yNode
		else: xNode.parent.left = yNode
		yNode.right = xNode
		xNode.parent = yNode
