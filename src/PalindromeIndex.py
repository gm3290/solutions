def isPalindrome(s, l, r):
    if s is None or l > r:
        return False

    while (l < r):
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


def palindromeIndex(s):
    if s is None or len(s) < 2:
        return -1
    l = 0
    r = len(s) - 1
    if isPalindrome(s, l, r):
        return -1
    while (l < r):
        if (s[l] != s[r]):
            if isPalindrome(s, l+1, r):
                return l
            if isPalindrome(s, l, r-1):
                return r
        l += 1
        r -= 1
    return -1


print(palindromeIndex('aaab'))
