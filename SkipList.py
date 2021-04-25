from random import randint, seed
from SkipNode import SkipNode

class SkipList:
	def __init__(self):
		self.head = SkipNode()
		self.len = 0
		self.maxHeight = 0

	def find(self, elem, update = None):
		if update == None:
			update = self.updateList(elem)
		if len(update) > 0:
			item = update[0].next[0]
			if item != None and item.val == elem:
				return item
		return None

	def isKeyExist(self, elem, update = None):
		return self.find(elem, update) != None

	def randomHeight(self):
		height = 1
		while randint(1, 2) != 1:
			height += 1
		return height

	def updateList(self, elem):
		update = [None]*self.maxHeight
		x = self.head
		for i in reversed(range(self.maxHeight)):
			while x.next[i] != None and x.next[i].val < elem:
				x = x.next[i]
			update[i] = x
		return update

	def insert(self, elem):
		_node = SkipNode(self.randomHeight(), elem)
		self.maxHeight = max(self.maxHeight, len(_node.next))
		while len(self.head.next) < len(_node.next):
			self.head.next.append(None)
		update = self.updateList(elem)            
		if self.find(elem, update) == None:
			for i in range(len(_node.next)):
				_node.next[i] = update[i].next[i]
				update[i].next[i] = _node
			self.len += 1

	def delete(self, elem):
		update = self.updateList(elem)
		x = self.find(elem, update)
		if x != None:
			for i in reversed(range(len(x.next))):
				update[i].next[i] = x.next[i]
				if self.head.next[i] == None:
					self.maxHeight -= 1
			self.len -= 1            

	def __repr__(self) -> str:
		return "SkipList Class"

	def __str__(self) -> str:
		return "Len - " + str(self.len) + "\nMax Height - " + str(self.maxHeight) + "\nElements-\n" + self.head.next.__str__()
