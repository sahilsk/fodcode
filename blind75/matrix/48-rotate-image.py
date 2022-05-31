"""
48. Rotate Image - Medium
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


"""
Solution:
https://www.youtube.com/watch?v=69URVVl51n8
Very easy :D
1. First reverse the rows
2. Then transpose: by diagonally switching elements

"""

from runner import runner


def rotate(matrix: list[list[int]]) -> None:
    print("Input:--\n", matrix)
    # Reversing rows is nothing but just reversing an array.
    # In this case arrow of list. Change list order

    # reverse matrix by rows
    i = 0
    j = len(matrix) - 1
    tmp = []
    while i < j:
        tmp = matrix[i]
        matrix[i] = matrix[j]
        matrix[j] = tmp
        i += 1
        j -= 1

    print("-> Reverse \n", matrix)

    # transpose i.e flip elements diagonally
    for i in range(0, len(matrix)):
        for j in range(i+1, len(matrix[0])):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    print("-> Output\n", matrix)


testcases = {
    "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]": (
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
    ),
    "[[7,4,1],[8,5,2],[9,6,3]]": ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
}

runner(rotate, testcases)
