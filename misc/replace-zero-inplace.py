"""
Dummy approach : O(n^2) because pop intermediate is o(n)
"""
def dummy(nums):
    numlen = len(nums)
    i, j = 0, len(nums) - 1

    while i < j:
        if nums[i] == 0:
            print("poping")
            nums.pop(i)
            nums.append(0)
            i -= 1
            j -= 1
        print(nums,i,j)
        i += 1
    return nums

"""
Super smart approach using one pointer only
Idea is simple:  increment index only if element is not zero. If i'ts zero

"""
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    lastNonZeroIdx = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZeroIdx] = nums[i]
            lastNonZeroIdx += 1

    for i in range(lastNonZeroIdx, len(nums)):
        nums[i] = 0




a = [0, 1, 5, 0, 0, 10, 100, -1]
a = [2, 1, 5, 0, 0, 10, 100, -1]

answer = moveZeroes(a)
# answer = dummy(a)
print(answer, a)
