# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List
NOT_FOUND = [-1, -1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indices = NOT_FOUND
        if nums:
            mid = len(nums) // 2

            if (0 <= mid < len(nums)) and nums[mid] == target:
                indices = [mid, mid]
                l_idx = mid-1
                while l_idx >= 0 and nums[l_idx] == target:
                    indices[0] = l_idx
                    l_idx -= 1

                r_idx = mid+1
                while r_idx < len(nums) and nums[r_idx] == target:
                    indices[-1] = r_idx
                    r_idx += 1
            elif (0 <= mid < len(nums)) and target < nums[mid]:
                indices = self.searchRange(nums[:mid], target)
            elif (0 <= mid < len(nums)) and target > nums[mid]:                
                new_indices = self.searchRange(nums[mid+1:], target)
                if new_indices == NOT_FOUND:
                    indices = NOT_FOUND
                else:
                    indices = [mid+1, mid+1]                    
                    indices = [sum(i) for i in zip(indices, new_indices)]

        return indices


# nums = [4,5,6,7,0,1,2]
# nums = [1]
# nums = [1, 3, 5]
# target = 3
# target = 0


# nums = [5,7,7,8,8,10]
# target = 8
# nums = [5,7,7,8,8,10]
# target = 6
nums = [1,2,3]
target = 3

sol_obj = Solution()
print(sol_obj.searchRange(nums, target))
