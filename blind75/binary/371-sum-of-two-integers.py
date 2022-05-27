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

"""

from runner import runner


def sumWithoutOperators(a:int, b:int) -> int:



testcases = {
   3:(1, 2,),
   5:(2,3)
}

runner(sumWithoutOperators, testcases)
