'''
https://www.geeksforgeeks.org/problems/implement-stack-using-array/1
'''


#########################################################################################

class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.item = []
        self.n = n


    def isEmpty(self):
        # Check if stack is empty
        return len(self.item) == 0
    
    
    def isFull(self):
        # Check if stack is full
        return len(self.item) == self.n
    
    
    def push(self, x):
        # Insert x at the top of the stack
        if not self.isFull():
            self.item.append(x)
    
    
    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return -1
        return self.item.pop()
    
    
    def peek(self):
        # Returns the top element of the stack
        if self.isEmpty():
            return -1
        return self.item[-1]
	
#########################################################################################