from typing import List
"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

https://www.youtube.com/watch?v=U8XENwh8Oy8&ab_channel=NeetCode


4 5 6 7  0 1 2
      7 mid  > l, l = mid + 1
      elif m < r:
          l = mid


"""



def search( nums:List[int], target:int) ->  int:
    left = 0
    right = len(nums) - 1
    
    '''
    4 5 6 7 0 1 2
              1

    m > l:
        l = mid + 1

    '''
    while left < right:
        mid = left + (right - left)//2

        print("seraching in :", left, right)
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid
    
    return left, right


print(search([4, 5, 6, 7, 0, 1, 2], 0) )

assert search([4, 5, 6, 7, 0, 1, 2], 0) ==  4
assert search([4, 5, 6, 7, 0, 1, 2], 3) ==  -1
assert search([1], 0) == -1