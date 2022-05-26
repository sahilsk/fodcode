from runner import runner

"""
152. Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

"""
Solution: https://youtu.be/tHNsZHXnYd4?t=711
"""


def maxProductSubarray(nums: list[int]) -> int:
    ans = nums[0]
    ma = ans
    mi = ans

    for i in range(1, len(nums)):
        if nums[i] < 0:
            # swap
            ma, mi = mi, ma
        ma = max(nums[i], ma * nums[i])
        mi = min(nums[i], mi * nums[i])

        ans = max(ans, ma)
    return ans


testcases = {6: ([2, 3, -2, 4],), 0: ([-2, 0, -1],), 2: ([-2, 0, -1, -2],)}
runner(maxProductSubarray, testcases)
