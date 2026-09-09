'''
https://www.geeksforgeeks.org/problems/implement-queue-using-array/1
'''


#########################################################################################

class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.item = []
        self.n = n

    
    def isEmpty(self):
        # Check if queue is empty
        return len(self.item) == 0

    
    def isFull(self):
        # Check if queue is full
        return len(self.item) == self.n


    def enqueue(self, x):
        # Enqueue
        if not self.isFull():
            self.item.append(x)

    
    def dequeue(self):
        # Dequeue
        if self.isEmpty():
            return -1
        return self.item.pop(0)

    
    def getFront(self):
        # Get front element
        if self.isEmpty():
            return -1
        return self.item[0]
       
    
    def getRear(self):
        # Get rear element
        if self.isEmpty():
            return -1
        return self.item[-1]
	
#########################################################################################