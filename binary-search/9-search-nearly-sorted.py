'''

Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array. Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].

For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved to previous position.

Example :
Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2 
Output is index of 40 in given array

'''

def searchnearlysorted(nums, target) -> int :
    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = l + (r-l)//2
        prev = mid - 1
        next = (mid + 1)%len(nums)
        if nums[mid] == target:
            return mid
        elif nums[prev] == target:
            return  prev
        elif nums[next] == target:
            return  next

        # move to other half of array by incrementing + 2
        elif nums[mid] > target:
            r = mid - 2
        elif nums[mid] < target:
            l = mid + 2

    return -1

nums = [10, 3, 40, 20, 50, 80, 70]
target = 70

print(searchnearlysorted(nums, target))