""""
FIND AN ELEMENT IN BITONIC ARRAY:

Given a bitonic sequence of n distinct elements, write a program to find a given element x in the bitonic sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.

Solution:   Find maximum element i.e find peak element, then run two max( bs(0, peak), bs(peak, end))

Examples:

Input :  arr[] = {-3, 9, 8, 20, 17, 5, 1};
         key = 20
Output : Found at index 3


"""

def searchbitonic(nums, target) -> int:

    l = 0
    r = len(nums) - 1
    


testcases = {
    1: ([1, 2, 3, 0], 2),
    0: ([1, 2, 3, 0], 1),
    4: ([1, 3, 6, 12, 4, 2], 4),
}

for result, input in testcases.items():
    print(f"Expected({result}): Output: ", searchbitonic(input[0], input[1]))

