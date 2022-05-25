from runner import runner
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
"""
"""
Three way to do this problem:
1. using hash in two pass: Store the hash and then in next pass, compare with hash data
2. Using hash but in ONE PASS: Add element as they come and at later index, you will find teh combination
3. sort the array and then compare start with end index
    if sum is greater than target , then end--, else start++
"""


def twosum(nums: list[int], target: int) -> list[int]:

    twosumhash = dict()

    for index, element in enumerate(nums):
        twosumhash[element] = twosumhash.get(element, []) + [index]

    # print(twosumhash)
    for idx, ele in enumerate(nums):
        nexttarget = target - ele

        found = twosumhash.get(nexttarget, [])
        if found:
            if idx in found:
                if len(found) > 1:
                    return [idx, found[1]]
            else:
                return [idx, found[0]]
    return [-1, -1]


def twosumsinglepass(nums: list[int], target: int) -> list[int]:

    whash = dict()
    for i, v in enumerate(nums):
        nexttarget = target - v
        # watchout for '0' element in teh hash, it resolves to FALSE ;)
        if whash.get(nexttarget, None) != None:
            return [i, whash[nexttarget]]
        whash[v] = i

    return [-1, -1]


def twosumsortedlogic(nums: list[int], target: int) -> list[int]:

    # create tuple to store  indexes to return after  sorting
    sortednums = []
    for i, v in enumerate(nums):
        sortednums.append((v, i))

    sortednums.sort()
    if len(nums) <= 1:
        return [-1, -1]

    i, j = 0, len(nums) - 1
    while i < j:
        tsum = sortednums[i][0] + sortednums[j][0]
        if tsum == target:
            return [sortednums[i][1], sortednums[j][1]]
        elif tsum > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]


testcases = {
    # result : inputs
    "[0,1]": ([3, 3], 6),
    "[1,2]": ([13, 7, 2, 15], 9),
    "[2,4]": ([1, 7, 2, 15, 2], 4)
}

nums = [3, 3]
target = 6

# print( twosum(nums, target))
runner(twosum, testcases)
print("Second method----")
runner(twosumsinglepass, testcases)
print("Third method----")
runner(twosumsortedlogic, testcases)
