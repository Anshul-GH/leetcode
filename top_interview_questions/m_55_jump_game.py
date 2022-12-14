# https://leetcode.com/problems/jump-game/
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        is_last_idx_accessible = False
        remaining_nums = nums[:-1]

        if 0 not in remaining_nums:
            is_last_idx_accessible = True
        else:
            for idx, val in enumerate(remaining_nums):
                if val == 0:
                    previous_values = remaining_nums[:idx]
                    len_prev_values = len(previous_values)
                    if any([(number-len_prev_values+indx) > 0 for number, indx in enumerate(previous_values)]):
                        is_last_idx_accessible = True
                    else:
                        is_last_idx_accessible = False
                        break

        return is_last_idx_accessible


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         is_last_idx_accessible = False
#         remaining_nums = nums[:-1]
#         remaining_len = len(remaining_nums)
#         recurring_sum = 0

#         if 0 not in remaining_nums:
#             is_last_idx_accessible = True
#         elif nums[0] != 0:
#             for idx, val in enumerate(remaining_nums):
#                 if val >= (remaining_len-idx):
#                     is_last_idx_accessible = True
#                 elif val == 0:
#                     if recurring_sum > idx:
#                         is_last_idx_accessible = True
#                     else:
#                         is_last_idx_accessible = False
#                         break

#                 recurring_sum += val

#         return is_last_idx_accessible
