'''
https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
'''

# Backtracking & Recursion #
#########################################################################################

class Solution:
    
    def findPathHelper(self,i, j, a, n, ans, move, vis):
        if i == n-1 and j == n-1:
            ans.append(move)
            return
        
        # downward
        if i + 1 < n and vis[i+1][j] == 0 and a[i+1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i+1,j,a,n,ans,move+"D",vis)
            vis[i][j] = 0
            
        # left
        if j - 1 >= 0 and vis[i][j-1] == 0 and a[i][j-1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i,j-1,a,n,ans,move+"L",vis)
            vis[i][j] = 0
        
        # right
        if j + 1 < n and vis[i][j+1] == 0 and a[i][j+1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i,j+1,a,n,ans,move+"R",vis)
            vis[i][j] = 0
        
        # upward
        if i - 1 >= 0 and vis[i-1][j] == 0 and a[i-1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i-1,j,a,n,ans,move+"U",vis)
            vis[i][j] = 0
        
        
    
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        # code here
        n = len(maze)
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]
        
        if maze[0][0] == 1:
            self.findPathHelper(0,0,maze,n,ans,"",vis)
        return ans
            
######################################################################################### 