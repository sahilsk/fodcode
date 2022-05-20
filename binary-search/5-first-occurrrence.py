from typing import List
"""
Find first occurrence of a number in a sorted array
"""


def firstoccur(nums:List[int], target:int) -> int:
    l = 0
    r = len(nums) - 1

    lastresult = -1
    while l <= r:
        mid = l + (r - l )//2

        if nums[mid] == target:
            lastresult = mid
            """"
            Instead of returning mid, we store last result
            and move left array
            """
            r = mid - 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return lastresult

testcases = {
    -1: ([2, 3], 1),
    0: ([2, 3], 2),
    2: ([1, 3, 5, 5, 5, 5, 67, 123, 125], 5),
    3: ([1, 3, 4, 5, 5, 5, 67, 123, 125], 5),
    4: ([1, 3, 4, 4, 5, 5, 67, 123, 125], 5)
}
for result, input in testcases.items():
    print(f"Excepted({result}) -> Output:", firstoccur(input[0],input[1]))
