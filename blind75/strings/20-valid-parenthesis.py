"""
20. Valid Parentheses - Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from runner import runner


def valid_parenthesis(s: str) -> bool:

    resultStore = []

    openBrackets = {"(": ")", "{": "}", "[": "]"}
    closeBrackets = {")": "(", "}": "{", "]": "["}

    for parenthesis in list(s):
        # open bracket case: add
        if parenthesis in openBrackets:
            resultStore.append(parenthesis)
        else:
            # close bracket case: compare and pop
            peak = resultStore[-1]
            if closeBrackets[parenthesis] != peak:
                return False
            else:
                resultStore.pop()

    if len(resultStore) == 0:
        return True
    else:
        return False


testcases = {"true": ["()"], "false": ["[[]]["]}

runner(valid_parenthesis, testcases)
