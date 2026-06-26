class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                self.hashMap[i][1] = value
                return
        
        self.hashMap.append([key, value])

    def get(self, key: int) -> int:
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                return self.hashMap[i][1]
        
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                del self.hashMap[i]
                return