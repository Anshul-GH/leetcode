# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        if nums:
            start = 0
            end = len(nums) - 1

        if start == end and nums[start] == target:
            index = start


        while start <= end:
            if nums[start] == target:
                index = start
                break
            else:
                start += 1

            if nums[end] == target:
                index = end
                break
            else:
                end -= 1

        return index


# nums = [4,5,6,7,0,1,2]
# nums = [1]
nums = [1, 3, 5]
# target = 0
target = 3
sol_obj = Solution()
print(sol_obj.search(nums, target))
