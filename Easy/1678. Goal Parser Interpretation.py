class Solution:
    '''
    Replace the keys with their decoed versions using the string method replace
    '''
    def interpret(self, command: str) -> str:
        decoded = command.replace("()", "o").replace("(al)", "al")

        return decoded
        