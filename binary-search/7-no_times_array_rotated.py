from typing import List
"""
How many times an array is rotated?

1st method:
number of times array rotated = index of minimum element

2nd method:
We can also solve by finding peak in array using BS and returning index(peak)+1

PS: WATCH OUT FOR DUPLICATES

[ 2, 5, 6, 8, 11, 12, 15, 18] =2 5 6 8

[11, 12, 15, 18, 2, 5, 6, 8]= 4
"""



# Find index of minimum element


def findpivot(nums:List[int]) -> int :

    l = 0
    r = len(nums) - 1
    if len(nums) == 0:
        return -1

    numlen = len(nums)
    while l <= r:
        # Edge case: if array is already sorted
        if nums[l] <= nums[r]:
            return l

        mid = l + (r-l)//2

        prev = mid - 1
        next = (mid + 1) % numlen
        if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
            #found minimum
            return mid
        elif nums[l] <= nums[mid]:
            # if left sorted, move to right
            l = mid + 1
        elif nums[mid] <= nums[r]:
            # if right is sorted, move to left
            r = mid - 1

    return -1

testcases = {
    1: ([18, 2, 5, 6, 8, 11, 12, 15],),
    4: ([11, 12, 15, 18, 2, 5, 6, 8],),
    3: ([10, 12, 15, 2, 5, 6, 8],),
    0: ([10, 12, 15],),
}
for result, input in testcases.items():
    print(f"Expected({result}): ", findpivot(input[0]))