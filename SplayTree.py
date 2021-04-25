#class SplayTree:
#	def __init__(self, height = 0, elem = None):
#		self.val = elem
#		self.next = [None]*height

from random import shuffle
from TreeNode import TreeNode
import time

class BinaryTree:
	"""A basic binary tree."""
	def __init__(self):
		self.root = None

	def insert(self, val, parent=None):
		"""Insert a new value in the tree. Takes one argument
		(the value to insert). Recursive binary search."""
		if (parent == None): parent = self.root
		if (parent == None):
			# root is null, make this the new root, done
			self.root = TreeNode(val)
			return
		elif (val < parent.val):
			if (parent.left == None):
				# insert to the left of the parent
				parent.left = TreeNode(val)
				return
			else:
				# search under the left
				self.insert(val, parent.left)
		else:
			if (parent.right == None):
				# insert to the right of the parent
				parent.right = TreeNode(val)
				return
			else:
				# search under the right
				self.insert(val, parent.right)

	def search(self, val, node=None):
		"""Find if a value is in the tree. Takes one argument
		(the value to find). If the value is in the tree, returns
		the node object. Otherwise returns None."""
		if (node == None):
			node = self.root
		if (node == None):
			# obviously it's not in an empty tree
			return None
		elif (val == node.val):
			return node
		elif (val < node.val):
			# Search left
			if (node.left != None):
				leftrv = self.search(val, node.left)
				if leftrv != None:
					return leftrv
		elif (val > node.val):
			if (node.right != None):
				rightrv = self.search(val, node.right)
				if rightrv != None:
					return rightrv
		return None

class SplayTree(BinaryTree):
	def search(self, val, node=None, p=None, g=None, gg=None):
		if (node == None): node = self.root
		if (node == None): return None
		elif (val == node.val): # If it's found, we need to move things around
			
			if (p != None):
				if (g == None):
					# Zig: swap node with its parent
					self.rotateUp(node, p, g)
				elif ((g.left == p and p.left == node) or
					  (g.right == p and p.right == node)):
					# Zig-zig: swap parent with grandparent
					self.rotateUp(p, g, gg)
					# Then swap node with parent
					self.rotateUp(node, p, gg)
				else:
					# Zig-zag: swap node with parent
					self.rotateUp(node, p, g)
					# Then swap node with grandparent
					self.rotateUp(node, g, gg)
			return node
		elif (val < node.val):
			# Search left
			if (node.left != None):
				leftrv = self.search(val, node.left, node, p, g)
				if leftrv != None:
					return leftrv
		elif (val > node.val):
			if (node.right != None):
				rightrv = self.search(val, node.right, node, p, g)
				if rightrv != None:
					return rightrv
		return None

	def rotateUp(self, node, parent, gp=None):
		"""Swap a node with its parent, keeping all child nodes
		(and grandparent node) in order."""
		if node == parent.left: 
			parent.left = node.right
			node.right = parent
			if (self.root == parent):
				self.root = node
		elif node == parent.right:
			parent.right = node.left
			node.left = parent
			if (self.root == parent):
				self.root = node
		else:
			print("This is impossible")

		if (gp != None):
			if (gp.right == parent):
				gp.right = node
			elif (gp.left == parent):
				gp.left = node

def test_splay_tree(treesize=100000, iters=20000):
	"""Just a simple test harness to demonstrate the speed of
	splay trees when a few items are searched for very frequently."""
	# Build a binary tree and a splay tree
	print("Building trees")
	bintree = BinaryTree()
	spltree = SplayTree()
	x = [i for i in range(0, treesize)]
	shuffle(x)
	for n in x:
		bintree.insert(n)
		spltree.insert(n)
	print("Done building")
	searches = x[-20:]

	# Search the splay tree 1000 times
	t1 = time.time()
	for i in range(0, iters):
		for n in searches:
			node = spltree.search(n)
			if (node == None):
				print("ERROR: %d" % n)
	t2 = time.time()
	print("Searched for 20 items %dx in splay tree: %.1f sec" % (iters, t2-t1))

	# Search the binary tree 1000 times
	t1 = time.time()
	for i in range(0, iters):
		for n in searches:
			node = bintree.search(n)
			if (node == None):
				print("ERROR: %d" % n)
	t2 = time.time()
	print("Searched for 20 items %dx in binary tree: %.1f sec" % (iters, t2-t1))

test_splay_tree()
