class Solution:
    '''
    find the idex of the end of the prefix
    reverse it and concatenate it with the remaining portion of the original string
    '''
    def reversePrefix(self, word: str, ch: str) -> str:
        end = word.find(ch)

        if end == -1:
            return word
        
        res = word[:end+1][::-1] + word[end+1:]

        return res
        