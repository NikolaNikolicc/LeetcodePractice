class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity

    def hash(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while self.map[index] != None and self.map[index].key != key:
            index += 1
            index = index % self.capacity

        if self.map[index] == None:
            self.map[index] = Pair(key, value)
            self.size += 1
            if float(self.size) / self.capacity >= 0.5:
                self.resize()
        else:
            self.map[index].value = value

    def get(self, key: int) -> int:
        index = self.hash(key)
 
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value

            index += 1
            index = index % self.capacity
        return -1


    def remove(self, key: int) -> bool:
        index = self.hash(key)

        while self.map[index] != None and self.map[index].key != key:
            index += 1
            index = index % self.capacity

        if self.map[index] == None:
            return False
        else:
            self.size -= 1
            self.map[index] = None
            return True


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        oldMap = self.map[:]
        self.capacity *= 2
        self.size = 0
        self.map = [None]*self.capacity

        for pair in oldMap:
            if pair:
                self.insert(pair.key, pair.value)

