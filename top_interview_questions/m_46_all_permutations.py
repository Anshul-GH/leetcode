# https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        all_perm = []

        for i in range(len(nums)):
            elem = nums[i]

            # remaining numbers
            rem_nums = nums[:i]+nums[i+1:]

            # append the elem to all permutations of remaining
            for p in self.permute(rem_nums):
                all_perm.append([elem]+p)

        return all_perm

