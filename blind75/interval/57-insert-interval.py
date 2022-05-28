"""
57. Insert Interval - Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

-----------------
Solution
- use mergeInterval()
    = insert the new interval -> sort it -> mergeInterval() : Too Slow
    - if empty , push-> continue
    - cmp (peak, interval), if overlapping insert new interval (peak[0], max(peak[1], interval[1]))
    - return stack
- Array is already sorted

"""

from runner import runner


def findIndex(intervals: list[list[int]], newInterval: list[int]):
    l = 0
    r = len(intervals) - 1
    lastClosestIdx = -1
    target = newInterval[0]
    while l <= r:
        mid = l + (r - l) // 2
        if intervals[mid][0] == target:
            lastClosestIdx = mid
            return lastClosestIdx
        elif intervals[mid][0] < target:
            lastClosestIdx = mid
            l = mid + 1
        elif intervals[mid][0] > target:
            r = mid - 1

    return lastClosestIdx


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[int]:

    if len(intervals) == 0:
        return [newInterval]

    ## find index to insert new interval in sorted array: O(logn)
    idx = findIndex(intervals, newInterval) + 1
    mergedIntervals = intervals[:idx] + [newInterval] + intervals[idx:]
    print(idx, mergedIntervals)

    ## sorting array o(nlogn)
    # mergedIntervals = intervals + [newInterval]
    # nlogn -> logn using bsearch
    # mergedIntervals = sorted(mergedIntervals, key=lambda x: x[0])
    # print(mergedIntervals)

    intervalStack = []
    for interval in mergedIntervals:
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
    "[[1,5],[6,9]]": ([[1, 3], [6, 9]], [2, 5]),
    "[[1,2],[3,10],[12,16]]": ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
}

runner(insert, testcases)
