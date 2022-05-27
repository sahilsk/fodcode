"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

==============
Solution:
t1  : nums[0],
t2 = nums[j]
t3 = -(t1+t2) - find in dict()
"""




from runner import runner

def  threesumTargetZero(nums:list[int]) -> list[list[int]]:
    
    if len(nums) <= 2:
        return []
    
    result = []
    # t1, t2 3
    for i in range(0, len(nums)):
        t1 = nums[i]

        j = i + 1
        prevstore = dict()

        while j < len(nums):
            t2 = nums[j]
            t3 = -(t1+t2)
            if prevstore.get(t3, None) != None:
                result.append([t1, t2, t3])
            else:
                prevstore[t2] = j
            
            j += 1
    return result
                



testcases = {
    "(0,2,3)" : ([1,2,6,4,5],),
    "[[-1,-1,2],[-1,0,1]]":([-1,0,1,2,-1,-4],)
}

runner(threesumTargetZero, testcases)
