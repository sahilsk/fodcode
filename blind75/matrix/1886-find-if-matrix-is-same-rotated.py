"""
1886. Determine Whether Matrix Can Be Obtained By Rotation -Easy
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
"""

"""
Solution
----------------

Rotate and compare 3 times: 90 , +90 , + 90

"""
from runner import runner


def findRotation( mat: list[list[int]], target: list[list[int]]) -> bool:
    def reverseMatrix(mat: list[list[int]]):
        mat = list(reversed(mat))
        return mat

    def transpose(mat: list[list[int]]):
        for i in range(len(mat)):
            for j in range(i + 1, len(mat[0])):
                tmp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = tmp

    if mat == target:
        return True

    mat = reverseMatrix(mat)
    transpose(mat)

    if mat == target:
        return True

    mat = reverseMatrix(mat)
    transpose(mat)

    if mat == target:
        return True

    mat = reverseMatrix(mat)
    transpose(mat)

    if mat == target:
        return True

    return False


testcases = {
    "true": (
        [[0, 1], [1, 0]],
        [[1, 0], [0, 1]],
    )
}

runner(findRotation, testcases)
