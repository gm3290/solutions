class Stack():
    def __init__(self):
        super().__init__()
        self.content = []


    def pop(self):
        data = self.content[-1]
        self.content.pop()
        return data

    def push(self, data):
        self.content.append(data)

    def pee(self):
        return self.content[-1]

    def isEmpty(self):
        return len(self.content)==0

class Queue():
    def __init__(self):
        super().__init__()
        self.firS = Stack()  # tale to head
        self.secS = Stack()  # head to tale

    def deq(self):
        if(self.secS.isEmpty()):
            self.mov()
        return self.secS.pop()

    def enq(self, data):
        self.firS.push(data)

    def mov(self):  #onLy 1 1to2    descpreated 2 2to1
        while(not self.firS.isEmpty()):
            self.secS.push(self.firS.pop())


    def printHead(self):
        if(self.secS.isEmpty()):
            self.mov()
        print(self.secS.pee())


q = Queue()
queries = input()

for i in range(int(queries)):
    s = input()
    l = s.split(' ')
    if (int(l[0]) == 1):
        q.enq(int(l[1]))
    elif (int(l[0]) == 2):
        q.deq()
    else:
        q.printHead()