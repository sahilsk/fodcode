"""
435. Non-overlapping Intervals - Medium

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
-------------------

Solution:  keep the one that is ending first
- Instead of merging, count the overlap as they occur
- If overlap, keep the one that is ending first coz, it's the greedy approach
- Explaination here: https://www.youtube.com/watch?v=nONCGxWoUfM&ab_channel=NeetCode

"""

from runner import runner


def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    # sort them : nlogn
    intervals.sort()

    # keep the one with ending first
    result = []
    removalCount = 0
    for interval in intervals:
        if len(result) == 0:
            result.append(interval)
            continue

        peak = result[-1]
        # are overlapping
        if peak[1] > interval[0]:
            removalCount += 1
            # overlapping
            # find one with ending first
            if peak[1] < interval[1]:
                # keep peak as it ending first
                continue
            else:
                # interval ending first
                result.pop()
                result.append(interval)
        else:
            # non-overlapping
            result.append(interval)
    
    # or substract length frm original length
    return removalCount


testcases = {1: ([[1, 2], [2, 3], [3, 4], [1, 3]],), 2: ([[1, 2], [1, 2], [1, 2]],)}
runner(eraseOverlapIntervals, testcases)
