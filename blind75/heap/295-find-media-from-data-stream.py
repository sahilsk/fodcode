""""
295. Find Median from Data Stream - Hard
https://www.youtube.com/watch?v=itmhHWaHupI&ab_channel=NeetCode


The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""


"""
Solution:

1. maintain: two arrays: small heap(maxheap), large heap(minHeap)
    1. Always add in maxheap
    2. if maxheap > minheap : do pop->push
    3. if size imbalance ie. (>1): pop(maxheap) -> push(minheap) i.e pop-> push

2. find median
    1. if len(maxheap)  + len(minheap) == even:
        maxheap[0] + minheap[0]//2
    2. else: maxheap[0]



"""

from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.mah = []
        self.mih = []

    def addNum(self, num: int) -> None:
        # add to mah first,
        # check if balance
        heappush(self.mah, -1 * num)

        # check if mah < mih
        if self.mih:
            if (-1 * self.mah[0]) > self.mih[0]:
                heappush(self.mih, -1 * heappop(self.mah))

        if len(self.mah) - len(self.mih) > 1:
            # balance
            heappush(self.mih, -1 * heappop(self.mah))
        elif len(self.mih) - len(self.mah) > 1:
            # balance
            heappush(self.mah, heappop(self.mih))

    def findMedian(self) -> float:
        total_elements = len(self.mih) + len(self.mah)
        if total_elements % 2 == 0:
            # even
            print("even: ", self.mah, self.mih)
            return (-self.mah[0] + self.mih[0]) / 2
        elif len(self.mih) > len(self.mah):
            return self.mih[0]
        else:
            return -1 * self.mah[0]


operations = [
    "addNum",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
]
stream = [1, 2, 3, 4, 5, 6]

medianFinder = MedianFinder()
result = []
for operation in operations:
    if operation == "addNum":
        if stream:
            medianFinder.addNum(stream[0])
            stream = stream[1:]
    elif operation == "findMedian":
        result.append(medianFinder.findMedian())

print(result)

"""
Output
[null, null, null, 1.5, null, 2.0]
"""
