import sys          #For Command Line Argument
import io           #Read File
import time
from HashTable import HashTable
from BST import BST
from SplayTree import SplayTree
from SkipList import SkipList
from RedBlackTree import RedBlackTree

def getInputFromFile(inputFileNameInSameDir: str):
	data = []
	with open(inputFileNameInSameDir) as f:
		for line in [line.rstrip() for line in f]:
			splittedData = line.replace('\t', ' ').split(" ", 1)
			data.append((int(splittedData[0]), splittedData[1].strip()))
	return data

def execute(selector: int, inputFileNameInSameDir: str):
	selector, data, dataStructure = selector or 4, getInputFromFile(inputFileNameInSameDir or "input1.txt"), None
	if selector == 0: #HashTable
		dataStructure = HashTable()
	elif selector == 1: #BST
		dataStructure = BST()
	elif selector == 2: #SplayTree
		dataStructure = SplayTree()
	elif selector == 3: #SkipList
		dataStructure = SkipList()
	elif selector == 4: #RBTree
		dataStructure = RedBlackTree()
	else:
		print(selector == '0')
		print(selector)
		print("Nothing is selected, so exiting")
		return
	executeWithData(dataStructure, data)
	if selector == 1 or selector == 2 or selector == 4:
		dataStructure.root.printTreeInorder()
		print("\n-------------------\nSorted Order Print Done")
	return dataStructure

def executeWithData(modelObject, data):
	for (choice, key) in data:
		if choice == 0:				#delete
			modelObject.delete(key)
		elif choice == 1:
			if not modelObject.isKeyExist(key):		# Not found, so insert
				modelObject.insert(key)
			else:					# Not found, so insert the data
				print("Searched and found key - " + key)

if __name__ == "__main__":
	start_time = time.time()
	if len(sys.argv)>1:
		try:
			selector = int(sys.argv[1])
			inputFileNameInSameDir = sys.argv[2] or "input1.txt"
		except Exception as e:
			selector = 0
			inputFileNameInSameDir = "input1.txt"
	else:
		selector = 0
		inputFileNameInSameDir = "input1.txt"
	print(execute(selector,inputFileNameInSameDir))
	print("Time: ", time.time() - start_time)
