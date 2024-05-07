class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        '''
        Split the string into an array of words
        For each word, check if any letter of the brokenLetters is in the word. If yes, skip that word with break
        Else, add the word to the count (else runs only if the inner for loop completes)

        '''
        count = 0
        words = text.split(" ")

        for word in words:
            for char in brokenLetters:
                if char in word:
                    break
            else:
                count += 1
        
        return count
        