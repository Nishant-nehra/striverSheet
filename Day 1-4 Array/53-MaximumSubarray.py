class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum=-10**9
        for item in nums:
            currSum=max(item,currSum+item)
            maxSum=max(currSum,maxSum)
        return maxSum