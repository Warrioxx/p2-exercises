class CircularBuffer:
    def __init__(self, cap):
        self.__list = []
        self.cap = cap

    def add(self, addition):
        self.__list.append(addition)
        if (len(self.__list) > self.cap):
            del self.__list[0]
    
    def __getitem__(self, index):
        return self.__list[index]

    def __len__(self):
        return len(self.__list)