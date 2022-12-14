# https://leetcode.com/problems/spiral-matrix/

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        traverse = []
        iteration = 0
        while matrix:
            # horizontal movement: left-right
            if iteration == 0 and matrix:
                traverse.extend(matrix[0])
                matrix = matrix[1:]
                iteration += 1
                iteration = iteration % 4
            
            # horizontal movement: right-left
            elif iteration == 2 and matrix:
                traverse.extend(matrix[-1][::-1])
                matrix = matrix[:-1]
                iteration += 1
                iteration = iteration % 4
            
            # vertical movement: top-down
            elif iteration == 1 and matrix:
                for idx, elem in enumerate(matrix):
                    if elem:
                        traverse.append(elem[-1])
                        matrix[idx] = elem[:-1]
                iteration += 1
                iteration = iteration % 4

            # vertical movement: bottom-up
            elif iteration == 3 and matrix:
                matrix = matrix[::-1] # reverse the matrix
                for idx,elem in enumerate(matrix):
                    if elem:
                        traverse.append(elem[0])
                        matrix[idx] = elem[1:]
                matrix = matrix[::-1] # reinstate matrix
                iteration += 1
                iteration = iteration % 4
    
        return traverse
