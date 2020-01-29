# Terminated due to timeout
class MyQueue(object):
    def __init__(self):
        self.lifo = list()
        self.fifo = list()
    
    def peek(self):
        return self.fifo[0]
        
    def pop(self):
        self.lifo.pop()
        self.fifo = self.fifo[1:]
               
    def put(self, value):
        self.fifo.append(value)
        self.lifo = [value] + self.lifo
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
