'''
https://www.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names-1587115621/1
'''


#########################################################################################

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        
        dict = {}
        
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        winner_vote = 0
        
        for key,value in dict.items():
            if value > winner_vote:
                winner_vote = value
        
        winner_name = min(key for key,value in dict.items() if value == winner_vote)

        return [winner_name, winner_vote]
	
#########################################################################################