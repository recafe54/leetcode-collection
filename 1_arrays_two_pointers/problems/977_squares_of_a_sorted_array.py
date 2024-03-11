class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        square_nums = [x**2 for x in nums]
        result = []

        while left <= right:
            if square_nums[left] > square_nums[right]:
                result.append(square_nums[left])
                left += 1
            else:
                result.append(square_nums[right])
                right -= 1
        
        return result[::-1]

"""
Pre-define result = [0] * n 

--> So we can travel in reveresed order 
while squaring & comparing 

--> for i in range(n - 1, -1, -1)
From: n-1 
To: 1 (exclude -1)
Step: -1 (Decreasing)

"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result