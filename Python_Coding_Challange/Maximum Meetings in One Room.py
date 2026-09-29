'''
https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1
'''

#########################################################################################

class Solution:
    def maxMeetings(self, s, f):
        # code here
        arr = []
        
        for i in range(len(s)):
            temp = [s[i],f[i],i+1]
            arr.append(temp)
            
        arr.sort(key = lambda x:(x[1],x[2]))
        
        meeting = []
        last_end = -1
        
        for start,end,j in arr:
            if last_end < start:
                meeting.append(j)
                last_end = end
                
        meeting.sort()
        
        return meeting
	
#########################################################################################