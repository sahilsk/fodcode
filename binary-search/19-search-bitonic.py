""""
FIND AN ELEMENT IN BITONIC ARRAY:

Given a bitonic sequence of n distinct elements, write a program to find a given element x in the bitonic sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.

Solution:   Find maximum element i.e find peak element, then run two max( bs(0, peak), bs(peak, end))

Examples:

Input :  arr[] = {-3, 9, 8, 20, 17, 5, 1};
         key = 20
Output : Found at index 3


"""

def searchBinary(nums, l, r, target):
    ascending = False

    if nums[l] < nums[r]:
        # increasing
        ascending = True

    while l <= r :
        mid = l + (r-l)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            if ascending:
                l = mid + 1
            else:
                r = mid - 1
        elif nums[mid] > target:
            if ascending:
                r = mid - 1
            else:
                l = mid + 1

    return -1





def searchbitonic(nums, target) -> int:

    l = 0
    r = len(nums) - 1
    peak = -1
    
    # find peak
    while l <= r:
        mid = l + (r-l)//2

        prev = mid - 1
        next = mid + 1
        if prev < 0:
            l = mid + 1
        elif next >= len(nums):
            r = mid - 1
        elif  nums[prev] < nums[mid] > nums[next]:
            peak = mid
            break
        elif nums[mid] > nums[prev]:
            l = mid + 1
        else: 
            r = mid - 1


    l1 = searchBinary(nums, 0, peak, target)
    l2 = searchBinary(nums, peak+1, len(nums)-1, target)
    return max(l1, l2)
    


testcases = {
    1: ([1, 2, 3, 0], 2),
    0: ([1, 2, 3, 0], 1),
    4: ([1, 3, 6, 12, 4, 2], 4),
}

for result, input in testcases.items():
    print(f"Expected({result}): Output: ", searchbitonic(input[0], input[1]))

