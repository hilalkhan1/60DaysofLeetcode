class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]
        return []
        