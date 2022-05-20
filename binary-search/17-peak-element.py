"""
FIND PEAK ELEMENT IN AN ARRAY:

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example :

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""



def searchpeak(nums) -> int:

    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = l + (r-l)//2

        prev = mid - 1
        next = mid + 1

        """
        if el in mid
            if peak, return mid
            if not, find l , r
        if at left cliff:
            if peak, return mid
            if not, find l, r
        if at right cliff:
            if peak, return mid
            if not,find l, r
        
        """
        if prev >= 0 and next < len(nums):
            if  nums[prev] < nums[mid]  > nums[next]:
                return mid
            elif nums[prev] > nums[mid]:
                r = mid - 1
            elif nums[next] > nums[mid]:
                l = mid + 1
        elif prev < 0 :
            if nums[mid] > nums[next]:
                return mid
            else:
                l = mid + 1

        elif next >= len(nums):
            if nums[mid] > nums[prev]:
                return mid
            else:
                r = mid - 1

    return -1


testcases = {
    2: ([1, 2, 3, 1], ),
    0: ([5, 4, 3, 2, 1], ),
}

for result, input in testcases.items():
    print(f"Expected({result}): Output: ", searchpeak(input[0]))
