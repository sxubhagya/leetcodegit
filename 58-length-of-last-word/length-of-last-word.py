class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        z = len(s)
        i = z - 1

        # Move i back to skip any trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Mark the end of the last word
        end = i

        # Move i back to find the beginning of the last word
        while i >= 0 and s[i] != ' ':
            i -= 1

        # Length of the last word
        return end - i

# Example usage:
# solution = Solution()
# print(solution.lengthOfLastWord("Hello World"))
