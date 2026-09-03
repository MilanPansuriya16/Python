'''
https://www.geeksforgeeks.org/problems/n-queen-problem0315/1
'''

# Backtracking & Recursion #
#########################################################################################
##########  GFG Solution ##########
class Solution:

    def isSafe(self,row,col,board,n):
        duprow = row
        dupcol = col
        
        # Upper-left diagonal
        while duprow >= 0 and dupcol >= 0:
            if board[duprow][dupcol] == "Q":
                return False
            duprow -= 1
            dupcol -= 1
        
        # Left side    
        duprow = row
        dupcol = col
        while dupcol >= 0:
            if board[duprow][dupcol] == "Q":
                return False
            dupcol -= 1
            
        # Lower-left diagonal
        duprow = row
        dupcol = col
        while duprow < n and dupcol >= 0:
            if board[duprow][dupcol] == "Q":
                return False
            duprow += 1
            dupcol -= 1
            
        return True
        
        
    def solve(self,col,board,ans,temp,n):
        if col == n:
            ans.append(temp[:])
            return
        
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                temp.append(row + 1) # GFG uses 1-based indexing
                self.solve(col+1,board,ans,temp,n)
                temp.pop()
                board[row] = board[row][:col] + "." +board[row][col+1:]
        
        
    def nQueen(self, n: int) -> list[list[int]]:
        # code here
        ans = []
        board = ["."*n for i in range(n)]
        self.solve(0,board,ans,[],n)
        
        return ans
#########################################################################################
##########  Leetcode Solution ##########


class Solution:

    def isSafe(self,row,col,board,n):
        duprow = row
        dupcol = col
        
        # Upper-left diagonal
        while duprow >= 0 and dupcol >= 0:
            if board[duprow][dupcol] == "Q":
                return False
            duprow -= 1
            dupcol -= 1
        
        # Left side    
        duprow = row
        dupcol = col
        while dupcol >= 0:
            if board[duprow][dupcol] == "Q":
                return False
            dupcol -= 1
            
        # Lower-left diagonal
        duprow = row
        dupcol = col
        while duprow < n and dupcol >= 0:
            if board[duprow][dupcol] == "Q":
                return False
            duprow += 1
            dupcol -= 1
            
        return True
        
        
    def solve(self,col,board,ans,n):
        if col == n:
            ans.append(list(board))
            return
        
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                self.solve(col+1,board,ans,n)
                board[row] = board[row][:col] + "." +board[row][col+1:]
        
    def nQueen(self, n: int) -> list[list[int]]:
        # code here
        ans = []
        board = ["."*n for i in range(n)]
        self.solve(0,board,ans,n)
        
        return ans
            
#########################################################################################              
