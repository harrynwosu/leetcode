class Solution:
    def dayOfYear(self, date: str) -> int:
        '''
        WHAT MAKES A LEAP YEAR?
        If the year is divisible by 400 it is a leap year
        If the year is divisible by 4 and NOT DIVISIBLE by 100 then it is a leap year
        Else, it is not a leap year
        '''
        res = 0
        rev_date = "-".join(date.split("-")[::-1])
        days = { 1 : 31, 3: 31, 4: 30, 5:31, 6: 30, 7: 31, 8: 31, 9: 30, 10:31, 11: 30, 12: 31}

        if int(rev_date[6:]) % 400 == 0:
            days[2] = 29
        elif int(rev_date[6:]) % 4 == 0 and int(rev_date[6:]) % 10:
            days[2] = 29
        else:
            days[2] = 28

        for i in range(1, int(rev_date[3:5])):
            res += days[i]
        
        res += int(rev_date[:2])


        return res
        