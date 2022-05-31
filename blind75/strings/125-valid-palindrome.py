"""
125. Valid Palindrome - Easy
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

from runner import runner


def validPalindrome(s: str) -> bool:

    s = s.lower()
    i = 0
    j = len(s) - 1

    alphaNumList = "abcdefghijklmnopqrstuvwxyz0123456789"

    while i < j:
        if s[i] not in alphaNumList:
            i += 1
            # use continue here to avoid checking for out-of-index-cases
            continue
        if s[j] not in alphaNumList:
            j -= 1
            continue

        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False

    return True


testcases = {"true": ("A man, a plan, a canal: Panama",), "false": ("race a car",)}
runner(validPalindrome, testcases)
