from turtle import left, right
from runner import  runner
"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Solution:

Method 1:

"""


'''
Naive method: 
    maintain list of Zeroes
'''
def productEceptSelf(nums:list[int]) -> list[int]:

    if len(nums) < 2:
        return nums

    zeroes = []
    totalproduct = 1
    for i, v in enumerate(nums):
        if v == 0:
            zeroes.append(i)
        else:
            totalproduct = totalproduct * v


    answer = []

    for i , v in enumerate(nums):
        if zeroes:
            if i in zeroes:
                if len(zeroes) == 1:
                    answer.append(totalproduct)
                else:
                    answer.append(0)
            else:
                answer.append(0)
        else:
            answer.append(totalproduct//v)

    return answer



'''
Pre-Sum Method: The good one

Calcualte leftProduct and Right product

nums = [1, 2, 3, 4 ]
output = [24, 12, 8, 6]

Leftproduct: [1, 1, 2, 6]
rightproduct:[24,12,4,1]

'''

def productExceptSelfPresum(nums:list[list]) -> list[int]:


    lastElement = 1
    leftProduct = []
    rightProduct = []

    # calculate leftProduct
    '''
    1, 2, 3, 4

    '''
    leftProduct=[1]




testcases = {
    "[24,12,8,6]": ([1, 2, 3, 4], ),
    # "[0,0,9,0,0]": ([-1, 1, 0, -3, 3], ),
    # "[1]": ([1],)
}
# runner(productEceptSelf, testcases)
runner(productExceptSelfPresum, testcases)
