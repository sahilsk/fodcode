from typing import List
def search( nums: List[int], target: int) -> int:

    left = 0
    right = len(nums) - 1
    print(nums)
    pivot_element = -1
    while left <= right:
        print("Iteration", left, right)
        if nums[left] <= nums[right]:
            print("found sorted",  left, right)
            pivot_element = left
            break
        mid = left + (right - left)//2
        prev = (mid - 1)
        nxt = (mid + 1) % len(nums)

        if nums[prev] > nums[mid] < nums[nxt]:
            pivot_element = mid
            break
        elif nums[left] <= nums[mid]:
            left = mid + 1
        elif nums[mid] <= nums[right]:
            right = mid - 1

    print("found pivot", pivot_element)

    start = 0
    end = pivot_element
    if nums[len(nums)-1]  >= target  >= nums[pivot_element + 1]:
        start = pivot_element + 1
        end = len(nums) - 1

    # print(start, end)
    while start <= end:
        mid = start + (end - start) //2

        # print(start, mid, end)
        if nums[mid] == target:
            
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


# print(search([4, 5, 6, 7, 0, 1, 2], 0))
# print(search([4, 5, 1, 2, 3], 1))
print(search([1,3], 1))
print(search([1,3], 0))
