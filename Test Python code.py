

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ''
        for i in strs:
            a = ''
            for j in i:
                a = a + j
                for k in range(len(strs)):
                    if a in strs[k+1]:
                        common_prefix = a

        return common_prefix
    
obj_1 = Solution()
obj_1.longestCommonPrefix(["Apple","Cppla","Dpplw"])