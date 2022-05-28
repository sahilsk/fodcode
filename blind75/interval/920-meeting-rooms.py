"""
https://www.lintcode.com/problem/920/

920 · Meeting Rooms

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 

----------------------------
Solution
1. O(n): Run i,j and keep comparing. If overlapping, return False (:
"""

from runner import runner


def can_attend_meetings(intervals: list[list[int]]) -> bool:
    # sort them: nlogn
    intervals.sort()

    resultSet = []

    i, j = 0, 1

    while j < len(intervals):
        cur = intervals[i]
        nxt = intervals[j]

        if cur[1] > nxt[0]:
            return False
        else:
            i += 1
            j += 1

    return True


testcases = {"false": ([[0, 30], [5, 10], [15, 20]],), "true": ([[5, 8], [9, 15]],)}
runner(can_attend_meetings, testcases)
