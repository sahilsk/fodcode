from runner import runner
"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
-------------------

Solutions:

1. kadane algorithms
2. currentMaxSum + maxSubarray[0] 
"""


"""
Smart Solution:
- Keep adding sum until < 0. If < 0, then reset the counter
- Remeber len(subarray) >= 1, So, eg. [-1] = -1
"""
def maxSubarrayCount(nums:list[int]) -> int:
    maxSubArray = nums[0]
    currentMaxSum = 0

    for num in nums:
        if currentMaxSum < 0:
            currentMaxSum = 0
        currentMaxSum += num
        maxSubArray = max(maxSubArray, currentMaxSum)
    
    return maxSubArray


"""
Kadane Algorithm
- max ( prev-subarray, currentElement)

"""
def maxSubarraySumKadane(nums: list[int]) -> int:
    maxcurrent = 0
    maxglobal = nums[0]
    for n in nums:
        maxcurrent = max(n, maxcurrent + n)
        maxglobal = max(maxcurrent, maxglobal)

    return maxglobal


testcases ={
    6: ([-2,1,-3,4,-1,2,1,-5,4],),
    1: ([1],),
    -3: ([-4, -3],),
    23:([5,4,-1,7,8],)
}


# runner(maxSubarrayCount, testcases)
runner(maxSubarraySumKadane, testcases)