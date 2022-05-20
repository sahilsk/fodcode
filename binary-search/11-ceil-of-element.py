'''
CEILING OF AN ELEMENT IN A SORTED ARRAY:

Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing order.
Write efficient functions to find floor and ceiling of x.

Examples :

For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
For x = 0:    floor doesn't exist in array,  ceil  = 1
For x = 1:    floor  = 1,  ceil  = 1
For x = 5:    floor  = 2,  ceil  = 8
For x = 20:   floor  = 19,  ceil doesn't exist in array

'''


def  searchCeil(nums, target) -> int:
    l = 0
    r = len(nums) - 1

    # if first element is greater than target
    if nums[0] > target:
        return 0
    if nums[r] < target:
        return -1

    lastres = -1
    while l <= r:
        mid= l + (r-l)//2

        if nums[mid] == target:
            lastres = mid
            return mid
        elif nums[mid] > target:
            lastres = mid
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1

    return lastres




testcases = {
    0: ([1,2,8, 10,10,12, 19], 0),
    1: ([0, 1,2,8, 10,10,12, 19], 1),
    2: ([1,2,8, 10,10,12, 19], 5),
    -1: ([1,2,8, 10,10,12, 19], 20),
}

for result, input in testcases.items():
    print(f"Expected({result}): ", searchCeil(input[0], input[1]))