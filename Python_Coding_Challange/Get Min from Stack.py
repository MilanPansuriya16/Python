'''
https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
'''


#########################################################################################

class SpecialStack:

    def __init__(self):
        # Define Stack
        self.item = []
        
    
    def push(self, x):
        # Add an element to the top of Stack
        if len(self.item) == 0:
            self.item.append([x,x])
        else:
            mini = min(self.item[-1][1],x)
            self.item.append([x,mini])
    
    def pop(self):
        # Remove the top element from the Stack
        if self.isEmpty():
            return -1
        return self.item.pop()

    
    def peek(self):
        # Returns top element of Stack
        if self.isEmpty():
            return -1
        return self.item[-1][0]
        
        
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.item) == 0

    
    def getMin(self):
        # Finds minimum element of Stack
        if len(self.item) == 0:
            return -1
        else:
            return self.item[-1][1]
	
#########################################################################################