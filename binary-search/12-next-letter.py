"""
Given an array of letters sorted in ascending order,
find the smallest letter in the the array which is greater than a given key letter.


"""


def nextletter(nums, target) -> int:

    l = 0
    r = len(nums) - 1

    lastres = -1
    while l <= r:
        mid = l + (r-1)//2
        if nums[mid] == target:
            l = mid + 1
        elif nums[mid] > target:
            lastres = mid
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1

    return lastres


arr=['a', 'c', 'f', 'h']
target = 'f'
print(nextletter(arr, target))

