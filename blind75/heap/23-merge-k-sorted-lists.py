"""
23. Merge k Sorted Lists - Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

from runner import runner
from heapq import heappush, heappop


def mergeKLists(lists: list[list[int]]) -> list[int]:

    result = []
    heapStore = []

    lists = [lst for lst in lists if len(lst) > 0]

    if len(lists) == 0:
        return []

    for i in range(len(lists)):
        heappush(heapStore, (lists[i][0], i))
        lists[i] = lists[i][1:]

    while heapStore:
        tmp = heappop(heapStore)
        result.append(tmp[0])

        if lists[tmp[1]]:
            heappush(heapStore, (lists[tmp[1]][0], tmp[1]))
            lists[tmp[1]] = lists[tmp[1]][1:]

    return result


testcases = {
    "[1,1,2,3,4,4,5,6]": ([[1, 4, 5], [1, 3, 4], [2, 6]],),
    "[]": ([[]],),
}

runner(mergeKLists, testcases)
