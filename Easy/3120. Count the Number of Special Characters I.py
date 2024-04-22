class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        letters = set(word)
        
        for char in letters:
            if char.islower() and char.upper() in letters:
                count += 1
        return count