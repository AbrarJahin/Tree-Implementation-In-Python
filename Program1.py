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
	selector, data, dataStructure = selector, getInputFromFile(inputFileNameInSameDir), None
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
		print("\n-------------------\nSorted Order Print Init\n")
		dataStructure.root.printTreeInorder()
		print("\n\n-------------------\nSorted Order Print Done")
		print("\n\n-------------------\nPrint In Tree View")
		dataStructure.root.indentPrint()
		print("\n\n-------------------\nPrint In Data Structure View")
	return dataStructure

def executeWithData(modelObject, data):
	for (choice, key) in data:
		if choice == 0:				#delete
			modelObject.delete(key)
		elif choice == 1:
			if not modelObject.isKeyExist(key):		# Not found, so insert
				modelObject.insert(key)
			else:					# Not found, so insert the data
				print("Searched and found key - " + key + ", so nothing inserted")

if __name__ == "__main__":
	start_time = time.time()
	if len(sys.argv)>1:
		try:
			selector = int(sys.argv[1])
			inputFileNameInSameDir = sys.argv[2]
		except Exception as e:
			print("CMD Argument read error, so default value shown")
			selector = 4
			inputFileNameInSameDir = "input1.txt"
	else:
		selector = 4
		inputFileNameInSameDir = "input1.txt"
	print(execute(selector,inputFileNameInSameDir))
	print("Time: ", time.time() - start_time)
