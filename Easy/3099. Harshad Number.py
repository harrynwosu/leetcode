class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = sum(map(int, str(x)))
        return -1 if x % total else total
        