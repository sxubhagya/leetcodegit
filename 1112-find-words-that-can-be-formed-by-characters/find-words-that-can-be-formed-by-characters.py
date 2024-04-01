class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)

            can_form = True
            for char, count in word_count.items():
                if char_count[char] < count:
                    can_form = False
                    break

            if can_form:
                total += len(word)
        
        return total