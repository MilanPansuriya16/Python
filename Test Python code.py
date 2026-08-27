class Solution:

    def solve(self, index , total , target , subset, nums, result):
        if total == target:
            subset.sort()
            subset = tuple(subset)
            result.add(subset)
            return
        elif total>target:
            return
        if index>= len(nums):
            return
        sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index+1, sum, target, subset, nums, result)
        sum = total
        subset.pop()
        self.solve(index+1, sum, target, subset, nums, result)

    def combutionsum2(self, nums, target):
        result = set()
        self.solve(0, 0, target, [], nums, result)
        return list(result)
obj = Solution()
print(obj.combutionsum2([1,1,2,1,2], 4))