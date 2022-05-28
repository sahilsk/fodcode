"""
371. Sum of Two Integers - Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

-----------
Solution
1. Collect carry using  (a&b) << 1
2. Sum them withount carry using a^b
3. do this while b != 0
4. return a

"""

from runner import runner


def sumWithoutOperators(a: int, b: int) -> int:

    while b != 0:
        # collect carry
        tmp = (a & b) << 1

        # sum them
        a = a ^ b

        # move next
        b = tmp
    return a


testcases = {
    3: (1, 2),
    5: (2, 3),
}

runner(sumWithoutOperators, testcases)
