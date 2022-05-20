from typing import List
'''
Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array.
If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.

Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element,
-if it is greater than high index element then copy high index in low index and double the high index.
-if it is smaller, then apply binary search on high and low indices found.

'''

"""
Hint: Find the start and End index ? 
    - by end * 2
"""


def findEndStartIndex(nums:List[int], target:int):
    start = 0
    end = start + 1

    # Find end using *2 
    while target >  nums[end]:
        start = end
        end = end * 2

    # Now run binary search

    l = start + 0
    r = end

    while l <= r:
        mid = l + (r - l)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        
    return -1
