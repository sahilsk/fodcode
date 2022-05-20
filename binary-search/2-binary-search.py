def search(nums,target):

    l = 0
    r = len(nums) - 1

    if len(nums) == 0:
        return -1

    while l <= r:
        mid = l + (r - l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


testcases = {
    2: ([0, 1, 3, 5, 6], 3),
   -1: ([], 3),
    0: ([2], 2),
}

for result, inputs in testcases.items():
    assert search(inputs[0], inputs[1]) == result