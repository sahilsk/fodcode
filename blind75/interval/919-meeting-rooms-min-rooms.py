"""
919 · Meeting Rooms II
https://www.lintcode.com/problem/919/
https://www.youtube.com/watch?v=FdzJmTCVyJU&ab_channel=NeetCode

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

(0,8),(8,10) is not conflict at 8


Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)


Example2
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
-------------------------
Solution
- keep track of #of meeting at given time by iteratring through two arrays, sorted Start and sorted End 
- counter++  if start < end, else counter --
- Run it till start array is finished. We don't have to worry about decrement meetings 
- Take the maximum of #counter value at any moment of time
"""

from runner import runner


def min_meeting_rooms(intervals: list[list[int]]) -> int:

    if len(intervals) == 0:
        return 0

    start = [x[0] for x in intervals]
    end = [x[1] for x in intervals]

    start.sort()
    end.sort()

    counter = 0
    i, j = 0, 0
    maxMeetings = 0
    # run loop till end of `start` array
    # as we don't care about end of meetings afterwards
    while i < len(intervals):

        # meeting started
        if start[i] < end[j]:
            counter += 1
            i += 1
        # meeting ending
        else:
            j += 1
            counter -= 1

        maxMeetings = max(counter, maxMeetings)

    return maxMeetings


testcases = {2: ([(0, 30), (5, 10), (15, 20)],), 1: ([(2, 7)],)}
runner(min_meeting_rooms, testcases)
