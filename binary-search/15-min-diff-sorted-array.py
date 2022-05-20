'''
Given a sorted array, find the element in the array which has minimum difference with the given number.
'''


import sys
from tkinter import W

"""
Brute force method: Find Ciel and Floor and find minimum among them.
But you are forgetting one important thing about bs. ;) 
"""
def findMinDiffElementBrute(nums, target):

    l = 0
    r = len(nums) - 1

    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums) - 1

    """
    If I can find Ceil and Floor for 'target', I can subtact them to get the minimum diff element?
    """
    # find floor

    lastfloor = -1
    ele_found = False
    while l <= r:
        mid = l + (r-l)//2

        if nums[mid] == target:
            element_found = True
            if element_found:
                return mid
            lastfloor = mid
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            lastfloor = mid
            l = mid + 1

    # Find ciel (reset old vars: l,r)
    lastciel = -1

    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] >= target:
            lastciel = mid
            r = mid - 1
        elif nums[mid] <= target:
            l = mid + 1

    if abs(nums[lastfloor] - target) < abs(nums[lastciel] - target):
        return lastfloor
    else:
        return lastciel



"""
Binary serach has a property. 
If element is not found, the left and right will point to its neighborrs ;)

"""


def findMinDiff(nums, target ) -> int :

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r-l)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1

    ldiff = abs(target -nums[l])
    rdiff = abs(target -nums[r])
    if  ldiff < rdiff:
        return l
    else:
        return r


testcases =  {
    4:  ([4,5, 6, 7, 10,11] , 9),
    3:  ([4,5, 6,7, 10, 11], 7),
    2:  ([4,5, 6, 10, 11], 7),
}


print("brute force: -----")
for result, input in testcases.items():
    print(f"Expected({result}): Output: ", findMinDiffElementBrute(input[0], input[1]))


print("Optimized Approache using BS property: -----")
for result, input in testcases.items():
    print(f"Expected({result}): Output: ", findMinDiff(input[0], input[1]))


