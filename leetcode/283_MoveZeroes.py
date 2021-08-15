class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroIdx = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[zeroIdx], nums[idx] = nums[idx], nums[zeroIdx]
                zeroIdx += 1
        
        for i in range(zeroIdx, len(nums)):
            nums[i] = 0
