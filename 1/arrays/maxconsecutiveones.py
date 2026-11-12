class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        biggest_streak = 0
        current_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
                if current_streak > biggest_streak:
                    biggest_streak = current_streak
            else:
                current_streak = 0
        
        return biggest_streak