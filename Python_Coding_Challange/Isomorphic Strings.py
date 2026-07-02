'''
https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1
'''


#########################################################################################

class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        
        map_s1_to_s2 = {}
        map_s2_to_s1 = {}
        
        for c1,c2 in zip(s1,s2):
            if c1 in map_s1_to_s2:
                if map_s1_to_s2[c1] != c2:
                    return False
            else:
                map_s1_to_s2[c1] = c2
                
            if c2 in map_s2_to_s1:
                if map_s2_to_s1[c2] != c1:
                    return False
            else:
                map_s2_to_s1[c2] = c1
            
        
        return True
	
#########################################################################################