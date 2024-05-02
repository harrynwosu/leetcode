class Solution:
    '''
    Use two pointers - one at start and one at end
    Check if their characters are equal. If yes, continue moving inward.
    If no, check if we have a palindrome between our pointers if we delete the char at either end of the substring contained by our pointers
    '''
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]:
                    return True
                else:
                    return False
        return True