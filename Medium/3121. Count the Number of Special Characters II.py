class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        '''
        For each character c, store the first occurrence of its uppercase and the last occurrence of its lowercase.
        If the last lowercase of a letter occurs before first uppercase (if it exists), increment count
        '''
        count = 0
        letters_dict = dict()
        
        for idx, char in enumerate(word):
            if char.islower():
                letters_dict[char] = idx
            else:
                if char not in letters_dict:
                    letters_dict[char] = idx
                    
        for char, idx in letters_dict.items():
            if char.islower() and char.upper() in letters_dict and idx < letters_dict[char.upper()]:
                count += 1
        
        return count
                
        