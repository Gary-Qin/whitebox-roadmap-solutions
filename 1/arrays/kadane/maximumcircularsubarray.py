class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        smallest = nums[0]
        largest = nums[0]
        current_smallest = 0
        current_largest = 0
        total_sum = 0

        for i in range(len(nums)):
            # kadane for max subarray
            if current_largest >= 0:
                current_largest += nums[i]
            else:
                current_largest = nums[i]
            if current_largest > largest:
                largest = current_largest

            # kadane for min subarray
            if current_smallest < 0:
                current_smallest += nums[i]
            else:
                current_smallest = nums[i]
            if current_smallest < smallest:
                smallest = current_smallest

            total_sum += nums[i]
        
        # in the case that all values are negative, the largest subarray would just be the largest value
        if largest < 0:
            return largest
        
        # total_sum - smallest gives the largest subarray with a loop
        return max(largest, total_sum - smallest)