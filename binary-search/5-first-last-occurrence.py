"""
Find first and last occurrence in sorted array
"""

def firstlastoccur(nums, target):

    l = 0
    r = len(nums) - 1

    if len(nums) == 0:
        return (-1, -1)
    
    while l <= r:
        mid = l + (r-l)//2

        if nums[mid] == target:
            # return mid: HOLD IT
            start, end = mid, mid
            while mid-1 >=0 and nums[mid] == nums[mid-1]:
                start = mid - 1
                mid = mid - 1
            while mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                end = mid + 1
                mid = mid + 1
            return (start, end)

        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1 
    return (-1, -1)


testcases = {
    (2,4): ([2, 4, 10, 10, 10, 18, 20], 10),
}

for result, inputs in testcases.items():
    answer = firstlastoccur(inputs[0], inputs[1])
    print(f"checking {inputs[0], inputs[1]}=={answer}->", answer == result)
