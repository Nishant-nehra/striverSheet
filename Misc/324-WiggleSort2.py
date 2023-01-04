class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        sorted_nums = sorted(nums)
        index = len(nums) - 1

        # Odd positions
        for i in range(1, len(nums), 2):
            nums[i] = sorted_nums[index]
            index -= 1
        
        # Even positions 
        for i in range(0, len(nums), 2):
            nums[i] = sorted_nums[index]
            index -= 1
        
        return nums