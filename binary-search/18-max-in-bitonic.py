"""
FIND MAXIMUM ELEMENT IN AN BITONIC ARRAY:

Problem statement:
Given a bitonic array find the maximum value of the array. An array is said to be bitonic if it has an increasing sequence of integers followed immediately by a decreasing sequence of integers.

HINT: problem is similar to finding peak and infact, has same solution

Example:

Input:
1 4 8 3 2

Output:
8

"""

def searchMaxbitonic(nums):

    l = 0
    r = len(nums) - 1

    if len(nums) < 3:
        return max(nums)

    while l <= r:
        mid = l + (r-l)//2
        next = mid + 1
        prev = mid - 1
        '''
        prev < 0:
            mid < next
        '''
        if prev < 0:
            l = mid + 1
        elif next >= len(nums):
            r = mid - 1
        elif nums[prev] < nums[mid]  > nums[next]:
            return mid
        elif nums[mid] < nums[next]:
            l = mid + 1
        else:
            r = mid - 1

    return -1

testcases = {
    2: ([1, 2, 3, 0], ),
    3: ([1, 3, 3, 12, 4, 2], ),
}

for result, input in testcases.items():
    print(f"Expected({result}): Output: ", searchMaxbitonic(input[0]))
