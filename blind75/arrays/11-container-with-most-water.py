""""
11. Container With Most Water

Solution: https://www.youtube.com/watch?v=UuiTKBwPgAo&ab_channel=NeetCode

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Solution:
    1. O(n2) will result in Time-exceet error
    2. Do it in o(n) i.e iterate matrix once .hhmmmm i.e Two pointers

    Final solution:
    1. Maximize the width: L=0, R=len(height), then find tallest pillars by movng L/R
    2. move  L or R , whichever is smaller (why? max area comes with max height. so, ignore  all small height towers believe there could be next big)
    3. if L == R , move either side, doesn't matter

"""
from runner import runner
def maxwatercontainer(height:list[int]) -> int:
    
    if len(height) <= 1:
        return 0
    
    l = 0
    r = len(height) - 1

    maxarea = 0
    while l < r:
        current_area = (r-l) * min(height[l], height[r])
        maxarea = max(maxarea, current_area)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    
    return maxarea


testcases = {
    1: ([1,1],),
    49:([1,8,6,2,5,4,8,3,7],)
}

runner(maxwatercontainer, testcases)

    
