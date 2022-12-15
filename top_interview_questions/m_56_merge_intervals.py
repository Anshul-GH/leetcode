# https://leetcode.com/problems/merge-intervals

from typing import List
import numpy as np

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        array = list(np.array(intervals).flatten())
        intervals = sorted(intervals, key=lambda x:x[0])

        result = [array[0]]
        array = array[1:]
        counter = 0

        while counter < len(array)-1:    
            if array[counter+1] <= array[counter]:
                counter += 2
            else:
                if array[counter] not in result:
                    result.append(array[counter])
                if array[counter+1] not in result:
                    result.append(array[counter+1])
                counter += 1

        if (array[-1] not in result) or (len(result) % 2 != 0):
            result.append(array[-1])

        result = list(np.array(result).reshape(len(result)//2, 2))
        result = [list(res) for res in result]

        return result
