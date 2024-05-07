class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        consonants = 'bcdfghjklmnpqrstvwxyz'
        v_count, c_count = 0, 0
        
        if len(word) < 3:
            return False
        
        for char in word:
            char = char.lower()
            if char in vowels:
                v_count += 1
            elif char in consonants:
                c_count += 1
            elif not char.isnumeric():
                return False
        
        return v_count >= 1 and  c_count >= 1
        