def isPalindrome(s: str):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False

    return True
