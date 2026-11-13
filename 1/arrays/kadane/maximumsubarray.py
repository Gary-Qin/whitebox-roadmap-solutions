class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        largest = nums[0]
        current_sum = 0
        for num in nums:
            if current_sum > 0:
                current_sum += num
            else:
                current_sum = num
            
            if current_sum > largest:
                largest = current_sum
        
        return largest