from typing import List
"""

FIND AN ELEMENT IN A ROTATED SORTED ARRAY:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4



Find an element in an rotated array in log(n) time

1. Find pivot element index first: pivot
2. Then run bs on both subarary and pick the result not giving -1
    or max(bs(0, pivot) , bs(pivot, end))

"""


def searchRotatedArray(nums:List[int], target:int) -> int :

    # find pivot element
    # search target element

    # fine pivot element

    l = 0
    r = len(nums) - 1

    minindex = -1
    while l <=  r:
        mid = l + (r-l)//2

        if nums[l] < nums[r]:
            minindex = l
            break
        prev = mid - 1
        next = (mid + 1 )%len(nums)
        # check if minimum
        if nums[mid] < nums[prev] and nums[mid] < nums[next]:
            # found min element
            minindex = mid
            break
        elif nums[l] <= nums[mid]:
            # search in other half i.e in unsorted territory
            l = mid + 1
        elif nums[mid] <= nums[r]:
            # search in other half  i.e in unsorted territory
            r = mid - 1

    print("minindex", minindex)
    s, r = 0, 0
    if nums[minindex] <= target  <= nums[len(nums)-1]:
        s = minindex
        r = len(nums)-1
    elif nums[0] <= target <= nums[minindex-1]:
        s = 0
        r = minindex-1
    else:
        # element do not exist in either of the subarray
        return -1


    print("Search index : ", s, r)
    while s <= r:
        mid = s + (r-s)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid -1
        else:
            s = mid + 1

    return -1


testcases = {
    1: ([1, 3], 3),
    0: ([11, 12, 15, 18, 2, 5, 6, 8], 11),
    2: ([3,1,2], 1),
    -1: ([1, 3], 0),
    4: ([4, 5, 6, 7, 0, 1, 2], 0)
}

for result, input in testcases.items():
    print("----------")
    print( searchRotatedArray(input[0], input[1]) , result)
