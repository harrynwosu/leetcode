class Solution:
    '''
    Split the string into an array using whitespaces as the separator
    Using list comprehension reverse each words in the split string array
    Join this result array of reversed words into a string, separating the words with a single space
    '''
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        return " ".join([word[::-1] for word in words])