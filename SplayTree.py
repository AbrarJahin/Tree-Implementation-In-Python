import sys
from SplayNode import SplayNode

class SplayTree:
	def __init__(self):
		self.root = None

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
		if y.left != None:
			y.left.parent = x

		y.parent = x.parent
		if x.parent == None:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

	# rotate right at node x
	def rightRotate(self, x):
		y = x.left
		x.left = y.right
		if y.right != None:
			y.right.parent = x
		
		y.parent = x.parent;
		if x.parent == None:
			self.root = y
		elif x == x.parent.right:
			x.parent.right = y
		else:
			x.parent.left = y
		
		y.right = x
		x.parent = y

	# Splaying operation. It moves x to the root of the tree
	def splayOperation(self, x):
		while x.parent != None:
			if x.parent.parent == None:
				if x == x.parent.left:
					# zig rotation
					self.rightRotate(x.parent)
				else:
					# zag rotation
					self.leftRotate(x.parent)
			elif x == x.parent.left and x.parent == x.parent.parent.left:
				# zig-zig rotation
				self.rightRotate(x.parent.parent)
				self.rightRotate(x.parent)
			elif x == x.parent.right and x.parent == x.parent.parent.right:
				# zag-zag rotation
				self.leftRotate(x.parent.parent)
				self.leftRotate(x.parent)
			elif x == x.parent.right and x.parent == x.parent.parent.left:
				# zig-zag rotation
				self.leftRotate(x.parent)
				self.rightRotate(x.parent)
			else:
				# zag-zig rotation
				self.rightRotate(x.parent)
				self.leftRotate(x.parent)

	# joins two trees s and t
	def joinTrees(self, firstTree, secondTree):
		if firstTree == None: return secondTree
		if secondTree == None: return firstTree
		x = self.maximum(firstTree)
		self.splayOperation(x)
		x.right = secondTree
		secondTree.parent = x
		return x

	# search the tree for the key k
	# and return the corresponding node
	def search(self, k):
		x = self.searchTreeHelper(self.root, k)
		if x != None:
			self.splayOperation(x)

	# find the node with the minimum key
	def minimum(self, node):
		while node.left != None:
			node = node.left
		return node

	# find the node with the maximum key
	def maximum(self, node):
		while node.right != None:
			node = node.right
		return node

	# insert the key to the tree in its appropriate position
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

	# delete the node from the tree
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

	# print the tree structure on the screen
	def print(self):
		self.printHelper(self.root, "", True)
	def printHelper(self, currPtr, indent, last):
		# print the tree structure on the screen
		if currPtr != None:
			sys.stdout.write(indent)
			if last:
			  	sys.stdout.write("R----")
			  	indent += "     "
			else:
				sys.stdout.write("L----")
				indent += "|    "

			print(currPtr.val)

			self.printHelper(currPtr.left, indent, False)
			self.printHelper(currPtr.right, indent, True)

if __name__ == '__main__':
	tree = SplayTree()
	tree.insert(33)
	tree.insert(44)
	tree.insert(67)
	tree.insert(5)
	tree.insert(89)
	tree.insert(41)
	tree.insert(98)
	tree.insert(1)
	tree.print()
	tree.search(33)
	tree.search(44)
	tree.print()
	tree.delete(89)
	tree.delete(67)
	tree.delete(41)
	tree.delete(5)
	tree.print()
	tree.delete(98)
	tree.delete(1)
	tree.delete(44)
	tree.delete(33)
	tree.print()