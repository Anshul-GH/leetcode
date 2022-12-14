# https://leetcode.com/problems/maximum-subarray/
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_sum = maximum_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(0, current_sum) + num
            maximum_sum = max(current_sum, maximum_sum)

        return maximum_sum

# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]

sol_obj = Solution()
print(sol_obj.maxSubArray(nums))
