class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_str = str(x)
        n = len(new_str)
        for i in range(n//2):
            if new_str[i] != new_str[n-i-1]:
                return False
        return True