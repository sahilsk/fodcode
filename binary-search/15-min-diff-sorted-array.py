'''
Given a sorted array, find the element in the array which has minimum difference with the given number.
'''


import sys
from tkinter import W

def findMinDiffElement(nums, target):

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

    # Find ciel
    lastciel = -1

    while l <= r:
        mid = l + (r-l)//2

        if nums[mid] > target:
            lastciel = mid
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1

    if abs(nums[lastfloor] - target) < abs(nums[lastciel] - target):
        return lastfloor
    else:
        lastciel


testcases =  {
    4:  ([4,5, 6, 7, 10,11] , 9),
    3:  ([4,5, 6,7, 10, 11], 7),
    2:  ([4,5, 6, 10, 11], 7),
}


for result, input in testcases.items():
    print(f"Expected({result}): Output: ", findMinDiffElement(input[0], input[1]))