class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pointer = 0
        for num in nums:
            if num != 0:
                nums[pointer] = num
                pointer += 1

        for i in range(pointer, len(nums)):
            nums[i] = 0
