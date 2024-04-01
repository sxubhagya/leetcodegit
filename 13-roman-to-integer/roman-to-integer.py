class Solution:
    def romanToInt(self, s: str) -> int:
        roman = ['I','V','X','L','C','D','M']
        number = [1, 5, 10, 50, 100, 500, 1000]
        combined = dict(zip(roman, number))
        total = 0
        prev = 0

        for char in reversed(s):
            value = combined[char]
            if value < prev:
                total -= value
            else:
                total += value
                prev = value
        return total
