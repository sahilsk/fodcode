"""
73. Set Matrix Zeroes - Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

"""
Solution
----
1. No extra space: i.e  you need to find a way to store the result in the matrix itself
2. Do it in constant time

Naive approach : o(m + n)
1. Create two dict: cols and rows , and iterate matrix finding matr[i][j] == 0, add to row/cols
2. Next, set all places to zero if i or j in rows or cols.

Better : o(1)
1. use same matrix

BECAREFUL:
- Do not set any cell with '0' to '#', or you will loose that row/col to be set to 0
- Do not skip any cell, as it'll lead to skipping of '0'

"""

from runner import runner


def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0 and matrix[i][j] != "#":

                # set cols zero
                for k in range(n):
                    if matrix[i][k] != 0:
                        matrix[i][k] = "#"

                # set rows to zero
                for k in range(m):
                    if matrix[k][j] != 0:
                        matrix[k][j] = "#"

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "#":
                matrix[i][j] = 0

    return matrix


testcases = {
    "[[0,0,0,0],[0,4,5,0],[0,3,1,0]]": ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],),
    "[[1,0,1],[0,0,0],[1,0,1]]": ([[1, 1, 1], [1, 0, 1], [1, 1, 1]],),
}

runner(setZeroes, testcases)
