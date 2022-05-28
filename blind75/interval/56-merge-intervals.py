"""
56. Merge Intervals - Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

from heapq import merge
from runner import runner


def mergeInterval(intervals):
    if len(intervals) <= 1:
        return intervals

    intervalStack = []
    for interval in intervals:
        if len(intervalStack) == 0:
            intervalStack.append(interval)
            continue

        # Overlapping
        peak = intervalStack[-1]
        if peak[1] >= interval[0]:
            # overlapping
            intervalStack.pop()
            intervalStack.append([peak[0], max(peak[1], interval[1])])
            continue

        # non-overlapping
        intervalStack.append(interval)

    return intervalStack


testcases = {
  "[[1,6],[8,10],[15,18]]" :([[1,3],[2,6],[8,10],[15,18]],),
    "[[1,5]]"        :([[1,4],[4,5]],)
}
runner(mergeInterval, testcases)