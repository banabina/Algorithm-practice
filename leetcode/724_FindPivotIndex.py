class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums) - nums[0]
        if leftSum == rightSum:
            return 0
        
        for idx in range(1, len(nums)):
            rightSum -= nums[idx]
            leftSum += nums[idx - 1]
            if leftSum == rightSum:
                return idx
        return -1

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         leftSum = 0
#         rightSum = sum(nums)
        
#         pastNum = 0
#         for idx in range(len(nums)):
#             num = nums[idx]
#             rightSum -= num
#             leftSum += pastNum
#             if leftSum == rightSum:
#                 return idx
#             pastNum = num
#         return -1