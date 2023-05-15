class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 1
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                res += 1
                nums[i] = nums[j]
        return res