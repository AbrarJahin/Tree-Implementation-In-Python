from random import randint, seed
from SkipNode import SkipNode

class SkipList:
	def __init__(self):
		self.head = SkipNode()
		self.len = 0
		self.maxHeight = 0

	def __repr__(self) -> str:
		return "SkipList Class"

	def __str__(self) -> str:
		return "Len - " + str(self.len) + "\nMax Height - " + str(self.maxHeight) + "\nElements-\n" + self.head.next.__str__()

	def search(self, key: str, update = None) -> SkipNode:
		if update == None:
			update = self.updateList(key)
		if len(update) > 0:
			item = update[0].next[0]
			if item != None and item.val == key:
				return item
		return None

	def isKeyExist(self, key, update = None) -> bool:
		return self.search(key, update) != None

	def getRandomHeight(self) -> int:
		height = 1
		while randint(1, 2) != 1: height += 1	#Possiblity 0.5 for each failure
		return height

	def insert(self, key: str)-> None:
		nodeToInsert = SkipNode(self.getRandomHeight(), key)
		self.maxHeight = max(self.maxHeight, len(nodeToInsert.next))
		while len(self.head.next) < len(nodeToInsert.next):
			self.head.next.append(None)
		update = self.updateList(key)
		if self.search(key, update) == None:
			for i in range(len(nodeToInsert.next)):
				nodeToInsert.next[i] = update[i].next[i]
				update[i].next[i] = nodeToInsert
			self.len += 1

	def delete(self, key: str) -> None:
		update = self.updateList(key)
		x = self.search(key, update)
		if x != None:
			for i in reversed(range(len(x.next))):
				update[i].next[i] = x.next[i]
				if self.head.next[i] == None:
					self.maxHeight -= 1
			self.len -= 1

	def updateList(self, key: str) -> None:
		update = [None]*self.maxHeight
		x = self.head
		for i in reversed(range(self.maxHeight)):
			while x.next[i] != None and x.next[i].val < key:
				x = x.next[i]
			update[i] = x
		return update