from runner import runner

"""
33. Search in Rotated Sorted Array
Medium

14456

912

Add to List

Share
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
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""


"""
Solution:
    1. Find min. element
    2. then do bsearch
"""


def searchRotated(nums: list[int], target) -> int:

    l = 0
    r = len(nums) - 1
    minindex = -1
    if nums[l] < nums[r]:
        # already sorted
        minindex = l

    while l <= r:
        mid = l + (r - l) // 2
        if nums[l] < nums[r]:
            minindex = l
            break
        prev = mid - 1
        if prev >= 0 and nums[mid] < nums[prev]:
            minindex = mid
            break
        elif nums[mid] >= nums[l]:
            l = mid + 1
        elif nums[mid] < nums[r]:
            r = mid - 1

    l, r = 0, len(nums) - 1
    if target >= nums[minindex] and target <= nums[r]:
        return bsearch(nums, minindex, r, target)
    else:
        return bsearch(nums, l, minindex, target)


def bsearch(nums: list[int], start: int, end: int, target: int) -> int:
    # 1 <= n <=1000
    l = start
    r = end

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1

    return -1


testcases = {
    4: ([4, 5, 6, 7, 0, 1, 2], 0),
    -1: ([1], 0),
}


runner(searchRotated, testcases)
