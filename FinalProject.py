import sys          #For Command Line Argument
import io           #Read File
from HashTable import HashTable
from BST import BST
import SplayTree
import SkipList
import RBTree

def getInputFromFile(inputFileNameInSameDir: str):
    data = []
    with open(inputFileNameInSameDir) as f:
        for line in [line.rstrip() for line in f]:
            splittedData = line.replace('\t', ' ').split(" ", 1)
            data.append((int(splittedData[0]), splittedData[1].strip()))
    return data

def execute(selector: int, inputFileNameInSameDir: str):
    selector, data, dataStructure = selector or 3, getInputFromFile(inputFileNameInSameDir or "input1.txt"), None
    if selector==0: #HashTable
        dataStructure = HashTable()
    elif selector == 1: #BST
        dataStructure = BST()
    elif selector == 2: #SplayTree
        print('SplayTree')
    elif selector == 3: #SkipList
        print("SkipList")
    elif selector == 4: #RBTree
        print("RBTree")
    executeWithData(dataStructure, data)
    print(dataStructure)

def executeWithData(modelObject, data):
    for (choice, key) in data:
        if choice == 0:#delete
            modelObject.delete(key)
        elif choice == 1:
            if not modelObject.isKeyExist(key):    # Search if exist
                modelObject.insert(key)
            else:                       # Not found, so insert the data
                print("Searched and found key - " + key)

def main():
    if len(sys.argv)>1:
        selector = sys.argv[1] or 0
        inputFileNameInSameDir = sys.argv[2] or "input1.txt"
    else:
        selector = 0
        inputFileNameInSameDir = "input1.txt"
    return execute(selector,inputFileNameInSameDir)

if __name__ == "__main__":
    main()