"""
680. Valid Palindrome II - Easy
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
 

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

from runner import runner


def validPalindrome(s: str) -> bool:
    def isPalindrome(s, i, j, delCount):

        if delCount > 1:
            return False

        if i >= j:
            return True

        if s[i] == s[j]:
            return isPalindrome(s, i + 1, j - 1, delCount)
        else:
            delCount += 1
            a = isPalindrome(s, i + 1, j, delCount)
            b = isPalindrome(s, i, j - 1, delCount)
            return a or b

    return isPalindrome(s, 0, len(s) - 1, 0)


testcases = {
    "true": ("aba",),
    "false": ("abc",),
    "truee": ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",)
}

runner(validPalindrome, testcases)
