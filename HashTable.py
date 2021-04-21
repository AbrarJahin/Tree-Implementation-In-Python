class HashTable:
    # default constructor
    def __init__(self, maxNoOfElement = 100):
        self.currentSize = 0
        self.maxSize = maxNoOfElement
        self.hashData = [None for _ in range(maxNoOfElement)]

    # a method for printing data members
    def __repr__(self) -> str:
        return "Size : " + str(self.currentSize) + "/" + str(self.maxSize)

    def __str__(self) -> str:
        return ', '.join(str(e) for e in self.hashData if e is not None)

    def getHashValue(self, keyString: str) -> int:
        currentVal = 0
        for val in [ord(ch) for ch in keyString]:
            currentVal = currentVal*26 + val
        return currentVal % self.maxSize

    def isKeyExist(self, key: str) -> bool:
        return self.hashData[self.getHashValue(key)] is not None

    def search(self, key: str) -> bool:
        return self.hashData[key]

    def insert(self, key: str) -> str:
        if self.isKeyExist(key):
            #raise Exception("Sorry, Data Already Exists, Need overwrite")
            print("Key Already Exists")
            self.currentSize -= 1
        self.hashData[self.getHashValue(key)] = key
        self.currentSize += 1

    def delete(self, key: str) -> None:
        if not self.isKeyExist(key):
            #raise Exception("Sorry, Data Not Exists")
            print("Key Not Found")
            self.currentSize += 1
        self.hashData[self.getHashValue(key)] = None
        self.currentSize -= 1

    #def insert(data):  #If dynamic size
    #    hash_key = Hashing(keyvalue)
    #    Hashtable[hash_key].append(value)