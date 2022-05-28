"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

from collections import Counter
from heapq import heappop, heappush
from runner import runner


def topKFrequent(nums: list[int], k: int) -> list[int]:

    cnums = Counter(nums)
    # el:count

    result = []

    for el, freq in cnums.items():
        heappush(result, (freq, el))
        if len(result) > k:
            heappop(result)

    answer = []
    while result:
        answer.append(heappop(result)[1])
    

    # FOR `ANY ORDER`` LAEVE IT
    return list(reversed(answer))


testcases = {"[1,2]": ([1, 1, 1, 2, 2, 3], 2), "[1]": ([1], 1)}
runner(topKFrequent, testcases)
