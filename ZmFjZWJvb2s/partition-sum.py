"""
416. Partition Equal Subset Sum - Medium
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that
 the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

from runner import runner


def partition(arr:list[int]) -> bool:

    tsum = sum(arr)
    if tsum % 2 != 0:
        return False

    target = tsum//2

    print(target)
    return findTargetDp(arr, target)


def findTargetDp(arr:int, target:int) -> bool:

    if target == 0:
        return True

    if target < 0:
        return False
    
    if len(arr) == 0:
        return False
    
    return findTargetDp(arr[1:], target-arr[0]) or findTargetDp(arr[1:], target)
    

testcases = {
    "t": ([1,5,11,5],),
    "F": ([1,2,3,5],),
    "Tr": ([1,2,3,4,5,6,7],)
}


runner(partition, testcases)