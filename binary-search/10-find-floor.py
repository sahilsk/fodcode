"""
FIND FLOOR OF AN ELEMENT IN A SORTED ARRAY:

Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x. Write efficient functions to find floor of x.

Example:

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
Output : 2
2 is the largest element in arr[] smaller than 5


"""


def floorOfElement(nums, target) -> int:
    l = 0
    r = len(nums) - 1

    lastmin = -1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lastmin = mid
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1

    return lastmin



nums = [1,2,8,10, 10, 12, 19]
target = 11

print( floorOfElement(nums, target))