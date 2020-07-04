class Array:
    def __init__(self,length):
        self.length = length
        self.array = []

    def insert(self,item):
        return self.array.append(item)

    def remove(self,index):
        return self.array.pop(index)

    def indexOf(self,item):
        for i in range(len(self.array)):
            if self.array[i] == item:
                return i
        return -1

    def print(self):
        print(self.array)