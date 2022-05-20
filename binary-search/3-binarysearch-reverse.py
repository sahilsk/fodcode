

def searchReverselySorted(nums, target):
    """
    [5 ,4 3 2 1]
    
    """

    l = 0
    r = len(nums) - 1
    if len(nums) == 0:
        return -1
    while l <= r:
        mid = l + (r - l )//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1

testcases = {
    4: ([20, 17, 15, 14, 13, 12, 10, 9, 8, 4], 13),
   -1: ([], 3),
    0: ([2,1], 2),
}

for result, inputs in testcases.items():
    answer = searchReverselySorted(inputs[0], inputs[1])
    print(f"checking {inputs[0], inputs[1]}=={answer}")
    assert answer == result